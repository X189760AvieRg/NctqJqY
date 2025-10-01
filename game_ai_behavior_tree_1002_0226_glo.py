# 代码生成时间: 2025-10-02 02:26:28
import abc
import enum
import inspect

"""
游戏AI行为树框架，用于定义和执行AI行为树。
"""


# 枚举类型，定义节点执行状态
class NodeStatus(enum.Enum):
    """
    NodeStatus枚举类，用于表示节点的执行结果。
    """
    SUCCESS = 1
    FAILURE = 2
    RUNNING = 3
    INVALID = 4


def check_validity(node):
    """
    检查节点是否有效，即是否实现了必要的方法。
    """
    if not inspect.isclass(node):
        raise TypeError('节点必须是类类型')
    required_methods = ['update']
    for method in required_methods:
        if not inspect.getattr_static(node, method, None):
            raise TypeError(f'节点{node.__name__}必须实现{method}方法')

class Node(metaclass=abc.ABCMeta):
    """
    节点基类，定义了节点必须实现的方法。
    """
    @abc.abstractmethod
    def update(self):
        """
        更新节点状态的抽象方法。
        """
        pass

class Composite(Node):
    """
    组合节点基类，可以包含其他节点。
    """
    def __init__(self):
        self.children = []

    def add_child(self, node):
        """
        添加子节点。
        """
        check_validity(node)
        self.children.append(node)

class Sequence(Composite):
    """
    顺序节点，按顺序执行子节点。
    """
    def update(self):
        for child in self.children:
            status = child.update()
            if status == NodeStatus.FAILURE:
                return NodeStatus.FAILURE
            elif status == NodeStatus.RUNNING:
                return NodeStatus.RUNNING
        return NodeStatus.SUCCESS

class Selector(Composite):
    """
    选择节点，选择第一个成功的子节点。
    """
    def update(self):
        for child in self.children:
            status = child.update()
            if status == NodeStatus.SUCCESS:
                return NodeStatus.SUCCESS
            elif status == NodeStatus.RUNNING:
                return NodeStatus.RUNNING
        return NodeStatus.FAILURE

class Action(Node):
    """
    动作节点，执行具体动作。
    """
    def __init__(self, action):
        self.action = action

    def update(self):
        try:
            self.action()
            return NodeStatus.SUCCESS
        except Exception as e:
            print(f'动作执行失败：{e}')
            return NodeStatus.FAILURE

# 示例用法
class GameAI:
    def move(self):
        print('移动')

    def attack(self):
        print('攻击')

    def defend(self):
        print('防御')

    def strategy(self):
        sequence = Sequence()
        sequence.add_child(Action(self.move))
        sequence.add_child(Action(self.attack))
        
        selector = Selector()
        selector.add_child(Action(self.defend))
        selector.add_child(sequence)
        return selector.update()

if __name__ == '__main__':
    ai = GameAI()
    status = ai.strategy()
    print(f'AI行为树执行结果：{status.name}')
