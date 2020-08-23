# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫三个类。

# 这个类可以使用如下形式为动物园增加一只猫：
# if __name__ == '__main__':
#     # 实例化动物园
#     z = Zoo('时间动物园')
#     # 实例化一只猫，属性包括名字、类型、体型、性格
#     cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
#     # 增加一只猫到动物园
#     z.add_animal(cat1)
#     # 动物园是否有猫这种动物
#     have_cat = getattr(z, 'Cat')

#---------------------------------------------------------------------------

# 动物园类
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
class Zoo(object):
    def __init__(self,name):
        self.animals = []
        self.name = name

    def add_animal(self,animal):
        if not type(animal).__name__ in self.animals:
            self.animals.append(type(animal).__name__)
            self.__dict__[type(animal).__name__] = animal
        else:
            print(f'Warning : {type(animal).__name__} exist!')

    def show_animals(self):
        for animal in self.animals:
            print(animal)

# 动物类
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
class animal(object):

    size_dict = {
        '小':1,
        '中':2,
        '大':3
    }

    is_fierce_dict = {
        '凶猛':True,
        '温顺':False
    }

    eat_meat_dict = {
        '食肉':True,
        '食草':False,
        '杂食':False
    }


    def __init__(self,eat_meat,size,is_fierce):
        self.eat_meat = animal.eat_meat_dict[eat_meat]
        self.size = animal.size_dict[size]
        self.is_fierce = animal.is_fierce_dict[is_fierce]
        if (self.size >=2) and (self.eat_meat == True) and (self.is_fierce == True):
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False

# 猫类
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
class Cat(animal):

    yell = '喵~喵~喵'
    suitbale_for_pet = True

    def __init__(self,name,eat_meat,size,is_fierce):
        super().__init__(eat_meat,size,is_fierce)
        self.name = name

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(type(have_cat))
    z.show_animals()
    cat2 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat2)
    z.show_animals()