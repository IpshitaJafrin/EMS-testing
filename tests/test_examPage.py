from pages.examPage import ExamPage

def test_exam_creation(logged_in_browser):
    exam_page = ExamPage(logged_in_browser)
    exam_page.open()
    exam_page.enter_exam_name("new exam to test")

    # add more actions/assertions here
