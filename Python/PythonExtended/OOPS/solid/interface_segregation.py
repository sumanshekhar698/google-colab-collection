from abc import ABC, abstractmethod


# Fat Interface
class WorkerBad(ABC):

    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def eat(self) -> str:
        pass

    @abstractmethod
    def sleep(self) -> str:
        pass


class RobotBad(WorkerBad):
    def work(self) -> str:
        return "Robo Working"


    def eat(self) -> str:
        raise NotImplementedError("Robots dont eat")


    def sleep(self) -> str:
        raise NotImplementedError("Robots dont sleep")



class Workable(ABC):
    @abstractmethod
    def work(self) -> str:
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self) -> str:
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self) -> str:
        return "human working"
    def eat(self) -> str:
        return "human eating"
    def sleep(self) -> str:
        return "human sleeping"


class RobotWorker(Workable):
    def work(self) -> str:
        return "robo working"


hw = HumanWorker()
rw = RobotWorker()

print(hw.sleep())
print(hw.eat())
print(hw.work())

print(rw.work())