"""CLI entrypoint for the Stage 1/2 scaffold."""

from chatgtp.core import MessageRequest, build_response


def main() -> None:
    """Run Stage 2 simple demo flow."""
    print("chatgtp Stage 1 foundation is initialized.")
    print("Stage 2 simple example:")
    response = build_response(MessageRequest(user_name="newcomer", topic="core modules"))
    print(response)


if __name__ == "__main__":
    main()
