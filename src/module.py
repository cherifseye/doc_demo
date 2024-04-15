class DummyClass:
    """
    This is a dummy class used for demonstration purposes.

    Attributes:
        attribute1 (int): Description of attribute1.
        attribute2 (str): Description of attribute2.

    Methods:
        method1(param1, param2): Description of method1.
        method2(): Description of method2.
    """

    def __init__(self, attribute1, attribute2):
        """
        Initializes the DummyClass with the given attributes.

        Let's add small modification here to check what will happen?/

        Args:
            attribute1 (int): The value for attribute1.
            attribute2 (str): The value for attribute2.
            attribute3 (str): The value for attribute3.
        """
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self, param1, param2):
        """
        Perform some operation using param1 and param2.

        Let's add small modification here to check what will happen?/

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.
        Returns:
            bool: True if operation was successful, False otherwise.
        """
        pass

    def method2(self):
        """
        Perform another operation.

        Returns:
            str: Some result from the operation.
        """
        pass
