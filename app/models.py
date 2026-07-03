from datetime import date, timedelta
# Create a Flashcard class with the following attributes
class Flashcard:
    # Initialize every attribute 
    def __init__(self, front : str, back : str, deck : str, interval_days : int = 1, next_review_date : date | None = None):
        self.front = front
        self.back = back
        self.deck = deck
        self.interval_days = interval_days
        # If next_review_date is not provided, set it to today's date
        if next_review_date is None:
            next_review_date = date.today()
        self.next_review_date = next_review_date
    
    def review(self, correct: bool) -> None:
        if correct:
            self.interval_days *= 2
            
        else:
            self.interval_days = 1
            
        self.next_review_date = date.today() + timedelta(days=self.interval_days)

    def is_due(self) -> bool:
        return date.today() >= self.next_review_date
