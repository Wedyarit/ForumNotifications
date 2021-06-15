import time

from utils import parsers, topic


def main():
    while True:
        support = parsers.support()
        if topic.is_new(support):
            support.support_to_webhook()

        question = parsers.questions()
        if topic.is_new(question):
            question.question_to_webhook()

        time.sleep(5.5 * 60)


if __name__ == '__main__':
    main()
