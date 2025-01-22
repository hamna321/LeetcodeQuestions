class Foo:
    def __init__(self):
        # Events to manage synchronization between threads
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        # Print the first message
        printFirst()
        # Signal that the first method is done
        self.first_done.set()

    def second(self, printSecond: Callable[[], None]) -> None:
        # Wait until the first method is done
        self.first_done.wait()
        # Print the second message
        printSecond()
        # Signal that the second method is done
        self.second_done.set()

    def third(self, printThird: Callable[[], None]) -> None:
        # Wait until the second method is done
        self.second_done.wait()
        # Print the third message
        printThird()


# Example usage functions
def printFirst():
    print("first", end="")

def printSecond():
    print("second", end="")

def printThird():
    print("third", end="")


# Function to initiate the threads and start the process
def run(nums: List[int]):
    foo = Foo()

    # Threads for first, second, and third
    t1 = threading.Thread(target=foo.first, args=(printFirst,))
    t2 = threading.Thread(target=foo.second, args=(printSecond,))
    t3 = threading.Thread(target=foo.third, args=(printThird,))

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()



