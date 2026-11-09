import json
import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from llm.llm import answer_question


logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


@require_POST
def get_response(request):
    if not request.content_type.startswith("application/json"):
        return JsonResponse({"error": "JSON 요청을 보내주세요."}, status=415)
    try:
        body = json.loads(request.body)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return JsonResponse({"error": "JSON 형식을 확인해주세요."}, status=400)
    query = body.get("query") if isinstance(body, dict) else None
    if not isinstance(query, str) or not query.strip() or len(query) > 500:
        return JsonResponse({"error": "1~500자 질문을 입력해주세요."}, status=400)
    try:
        return JsonResponse({"response": answer_question(query.strip())})
    except Exception:
        logger.exception("Question answering failed")
        return JsonResponse({"error": "답변을 생성하지 못했습니다. 잠시 후 다시 시도해주세요."}, status=503)
