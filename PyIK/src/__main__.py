import sys

if __name__ == "__main__":
    from PyIK import Kinectics
    app = Kinectics()
    while not app.stopped:
        app.tick()
