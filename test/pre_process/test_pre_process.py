from src.pre_process import pre_process


def test_comments_and_directives():
    with open("test/pre_process/main.c") as input_file:
        with open("test/pre_process/main.solved.c") as output_file:
            input_text = input_file.read()
            output_text = output_file.read()
            assert pre_process(input_text) == output_text
