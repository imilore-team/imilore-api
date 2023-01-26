from os import environ

import telebot

from src.init import db
from src.models.feedback import InFeedbackModel
from src.tables.feedback import Feedback


class FeedbackProvider:
    bot = telebot.TeleBot(environ["BOT_TOKEN"]) if environ["BOT_TOKEN"] else None
    RECIVER_ID = environ["RECIVER_ID"]


    @classmethod
    def add_feedback(cls, feedback: InFeedbackModel):
        db.add(Feedback(email=feedback.email, description=feedback.description))
        return feedback

    @classmethod
    def send_to_telegram(cls, feedback: InFeedbackModel):
        if cls.bot is not None:
            try:
                cls.bot.send_message(
                    cls.RECIVER_ID, 
                    f"`{feedback.email}`\n{feedback.description}",
                    parse_mode="MarkdownV2"
                )
            except Exception as ex:
                print(ex)
        return feedback