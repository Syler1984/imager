import sys

from app import ImagerApplication


if __name__ == '__main__':

    argv = [sys.argv[0]] # TODO: Expand on arguments (and their contents) passed to the application class.

    app = ImagerApplication(argv)

    sys.exit(app.exec_())
