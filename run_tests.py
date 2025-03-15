import subprocess

def run_tests():
    subprocess.run(['python', 'tests/test_add_task.py'])
    subprocess.run(['python', 'tests/test_delete_task.py'])
    subprocess.run(['python', 'tests/test_show_tasks.py'])
    subprocess.run(['python', 'tests/test_complete_task.py'])

if __name__ == "__main__":
    run_tests()