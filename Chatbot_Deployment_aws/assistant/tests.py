import json
import os
from unittest.mock import patch

from django.test import Client, TestCase
from llm.llm import NO_ANSWER, answer_question


class AssistantAppTests(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_page_and_csrf_protection(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, "가상 문서")
        self.assertEqual(self.client.post("/query/", data="{}", content_type="application/json").status_code, 403)

    @patch("assistant.views.answer_question", return_value="가상 답변")
    def test_query_validation_and_response(self, answer):
        self.client.get("/")
        token = self.client.cookies["csrftoken"].value
        headers = {"HTTP_X_CSRFTOKEN": token}
        valid = self.client.post("/query/", data=json.dumps({"query": "휴가는?"}),
                                 content_type="application/json", **headers)
        self.assertEqual(valid.status_code, 200)
        self.assertEqual(valid.json()["response"], "가상 답변")
        self.assertEqual(answer.call_count, 1)
        invalid = self.client.post("/query/", data=json.dumps({"query": ""}),
                                   content_type="application/json", **headers)
        self.assertEqual(invalid.status_code, 400)
        malformed = self.client.post("/query/", data="{", content_type="application/json", **headers)
        self.assertEqual(malformed.status_code, 400)

    def test_offline_answer_uses_sample_document_and_abstains(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": ""}):
            self.assertIn("sample_policy.txt", answer_question("휴가는 어떻게 신청하나요?"))
            self.assertEqual(answer_question("급여는 언제 지급하나요?"), NO_ANSWER)
