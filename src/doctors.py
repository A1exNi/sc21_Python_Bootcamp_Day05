from threading import Lock, Thread


class Screwdriever:
    my_number: int = None
    my_state: Lock = None

    def __init__(self, number: int):
        self.my_number = number
        self.my_state = Lock()


class Doctor(Thread):
    my_number: int = None
    my_screwdriever: Screwdriever = None
    left_screwdriver: Screwdriever = None

    def __init__(
        self,
        number: int,
        screwdriever1: Screwdriever,
        scredriever2: Screwdriever
    ) -> None:
        self.my_number = number
        self.my_screwdriever = screwdriever1
        self.left_screwdriver = scredriever2
        super().__init__()

    def run(self):
        self.my_screwdriever.my_state.acquire()
        self.left_screwdriver.my_state.acquire()
        print(f'Doctor {self.my_number}: BLAST!')
        self.my_screwdriever.my_state.release()
        self.left_screwdriver.my_state.release()


def main():
    doctors = list()
    screwdrievers = list()
    for i in range(9, 14):
        screwdrievers.append(Screwdriever(i))
    for i in range(9, 13):
        doctors.append(
            Doctor(
                i,
                screwdrievers[i-9],
                screwdrievers[i-8]
            )
        )
    doctors.append(
        Doctor(
            13,
            screwdrievers[0],
            screwdrievers[4]
        )
    )
    for doctor in doctors:
        doctor.start()
    for doctor in doctors:
        doctor.join()


if __name__ == '__main__':
    main()
