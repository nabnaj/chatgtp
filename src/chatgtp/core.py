"""Core application logic for Stage 2 examples."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MessageRequest:
    """Input payload for generating a response message."""

    user_name: str
    topic: str


def build_response(request: MessageRequest) -> str:
    """Return a deterministic demo response for Stage 2.

    This intentionally keeps logic simple while showing where domain logic lives.
    """
    cleaned_name = request.user_name.strip() or "friend"
    cleaned_topic = request.topic.strip() or "the project"
    return (
        f"Hi {cleaned_name}! "
        f"Stage 2 is active and ready to discuss {cleaned_topic}."
    )
