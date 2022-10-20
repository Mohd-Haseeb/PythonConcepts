class Blockchain:
    def __init__(self, tutor, fee) -> None:
        self.tutor = tutor
        self.fee = fee

    def __repr__(self) -> str:
        return f"<Blockchain {self.tutor} : {self.fee}>"


class Course:
    def __init__(self) -> None:
        self.coursesEnrolled = []

    def __len__(self):
        return len(self.coursesEnrolled)

    def enroll_course(self, name):
        if not isinstance(name, Blockchain):
            raise TypeError(f"Tried to add {name.__class__.__name__} to Course, but you can only add `Blockchian` object ")
        self.coursesEnrolled.append(name)

ineuron = Course()

batch1 = Blockchain('tesuko',4000)

ineuron.enroll_course(batch1)
print(len(ineuron))