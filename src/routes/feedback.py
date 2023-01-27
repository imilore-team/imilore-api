from fastapi import APIRouter

from src.models.feedback import InFeedbackModel
from src.providers.feedback import FeedbackProvider


router = APIRouter()


@router.post("/send_feedback")
def post_send_feedback(feedback: InFeedbackModel) -> bool:
    FeedbackProvider.send_to_telegram(FeedbackProvider.add_feedback(feedback))
    return True