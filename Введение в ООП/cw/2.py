class Button:
    def __init__(self):
        self.click_count_ = 0

    def click(self):
        self.click_count_ += 1

    def reset(self):
        self.click_count_ = 0

    def click_count(self):
        return self.click_count_

