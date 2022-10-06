class Grade_st:
    def __init__(self,grade):
        self.grade = grade
    def get_grade(self):
        """
        >>> g = Grade_st(80)
        >>> g.get_grade()
        'A'
        >>> g = Grade_st(70)
        >>> g.get_grade()
        'B'
        >>> g = Grade_st(60)
        >>> g.get_grade()
        'C'
        >>> g = Grade_st(50)
        >>> g.get_grade()
        'D'
        >>> g = Grade_st(40)
        >>> g.get_grade()
        'F'
        """
        if self.grade >= 80:
            return 'A'
        elif self.grade >= 70:
            return 'B'
        elif self.grade >= 60:
            return 'C'
        elif self.grade >= 50:
            return 'D'
        else:
            return 'F'

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)