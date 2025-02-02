import os
import sys


def setup_environment():
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"
    os.system("bash setup.sh")

    # 설치 확인
    try:
        import whisper

        print("Whisper version:", whisper.__version__)
        return True
    except ImportError as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    setup_environment()
