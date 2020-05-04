from logic_utils import *

''' Atom and Conectors'''
class Atom(Formula):

    __slots__ = ['proposition','value_atom', 'repr_of_atom']

    def __init__(self, proposition, value_atom=None):
        self.proposition = proposition
        self.value_atom = value_atom
        self.repr_of_atom = Utils.repr_of_atom()
        
    def __str__(self):
        return self.proposition

    def __repr__(self):
        return self.repr_of_atom

    @property
    def value(self):
        return self.value_atom
    
    @value.setter
    def value(self, value):
        self.value_atom = value
        print("O valor da proposição '{}' foi setado para {}.".format(
            repr(self),
            value
        ))

    @value.deleter
    def value(self):
        self.value_atom = None
        print("O valor da proposição '{} foi setado para None".format(
            repr(self)
        ))

    @property
    def length(self):
        return 1
    
    @length.setter
    def length(self, length):
        print("Não é possivel setar o tamanho deste átomo!")

    @length.deleter
    def lenth(self):
        print("Não é possivel deletar este átomo!")

    @property
    def sub_formula(self):
        return (repr(self))   
    
    @sub_formula.setter
    def sub_formula(self, sub_formula):
        print("Não é possivel setar a sub-fórmula deste átomo!")

    @sub_formula.deleter
    def sub_formula(self):
        print("Não é possivel deletar a sub-fórmula deste átomo!")


class NOT(Formula):

    __slots__ = ['__right']

    def __init__(self, right:Formula):
        Utils.verified_propositions(right)
        self.__right = right

    def __str__(self):
        return "Não {}".format(
            str(self.__right).lower()
        )

    def __repr__(self):
        return "(~{})".format(
            repr(self.__right),
        )

    @property
    def value(self): 
        if self.__right.value == None:
            return 'O valor de algum átomo não foi setado'
        return not self.__right.value

    @value.setter
    def value(self, value):
        print("Não é possivel alterar o valor lógico desta fórmula!")
    
    @value.deleter
    def value(self):
        print("Não é possivel deletar o valor lógico desta fórmula!")

    @property
    def length(self):
        return self.__right.length + 1

    @length.setter
    def length(self, length):
        print("Não é possivel alterar o tamanho desta fórmula!")
    
    @length.deleter
    def length(self):
        print("Não é possivel deletar o tamanho desta fórmula!")

    @property
    def sub_formula(self):
        set_of_formulas = list(self.__right.sub_formula)
        set_of_formulas.append(repr(self))
        return sorted(set(set_of_formulas))

    @sub_formula.setter
    def sub_formula(self, sub_formula):
        print("Não é possivel alterar a sub-fórmula desta fórmula!")

    @sub_formula.deleter
    def sub_formula(self):
        print("Não é possivel deletar a sub-fórmula desta fórmula!")



class AND(Formula):

    __slots__ = ['__right', '__left']

    def __init__(self, right:Formula, left:Formula):
        Utils.verified_propositions(right)
        Utils.verified_propositions(left)
        self.__right = right
        self.__left = left 

    def __str__(self):
        return "{} e {}".format(
            self.__right,
            str(self.__left).lower()
        )

    def __repr__(self):
        return "({} ^ {})".format(
            repr(self.__right),
            repr(self.__left)
        )

    @property
    def value(self): 
        if self.__right.value == None or self.__left.value == None:
            return 'O valor de algum átomo não foi setado'
        return self.__right.value and self.__left.value
    @value.setter
    def value(self, value):
        print("Não é possivel alterar o valor lógico desta fórmula!")
    
    @value.deleter
    def value(self):
        print("Não é possivel deletar o valor lógico desta fórmula!")

    @property
    def length(self):
        return self.__right.length + self.__left.length + 1

    @length.setter
    def length(self, length):
        print("Não é possivel alterar o tamanho desta fórmula!")
    
    @length.deleter
    def length(self):
        print("Não é possivel deletar o tamanho desta fórmula!")

    @property
    def sub_formula(self):
        set_of_formulas = list(self.__right.sub_formula)
        set_of_formulas += self.__left.sub_formula
        set_of_formulas.append(repr(self))
        return sorted(set(set_of_formulas))

    @sub_formula.setter
    def sub_formula(self, sub_formula):
        print("Não é possivel alterar a sub-fórmula desta fórmula!")

    @sub_formula.deleter
    def sub_formula(self):
        print("Não é possivel deletar a sub-fórmula desta fórmula!")


class OR(Formula):

    __slots__ = ['__right', '__left']

    def __init__(self, right:Formula, left:Formula):
        Utils.verified_propositions(right)
        Utils.verified_propositions(left)
        self.__right = right
        self.__left = left 

    def __str__(self):
        return "{} ou {}".format(
            self.__right,
            str(self.__left).lower()
        )

    def __repr__(self):
        return "({} v {})".format(
            repr(self.__right),
            repr(self.__left)
        )

    @property
    def value(self): 
        if self.__right.value == None or self.__left.value == None:
            return 'O valor de algum átomo não foi setado'
        return self.__right.value or self.__left.value

    @value.setter
    def value(self, value):
        print("Não é possivel alterar o valor lógico desta fórmula!")
    
    @value.deleter
    def value(self):
        print("Não é possivel deletar o valor lógico desta fórmula!")

    @property
    def length(self):
        return self.__right.length + self.__left.length + 1

    @length.setter
    def length(self, length):
        print("Não é possivel alterar o tamanho desta fórmula!")
    
    @length.deleter
    def length(self):
        print("Não é possivel deletar o tamanho desta fórmula!")

    @property
    def sub_formula(self):
        set_of_formulas = list(self.__right.sub_formula)
        set_of_formulas += self.__left.sub_formula
        set_of_formulas.append(repr(self))
        return sorted(set(set_of_formulas))

    @sub_formula.setter
    def sub_formula(self, sub_formula):
        print("Não é possivel alterar a sub-fórmula desta fórmula!")

    @sub_formula.deleter
    def sub_formula(self):
        print("Não é possivel deletar a sub-fórmula desta fórmula!")

class THEN(Formula):

    __slots__ = ['__right', '__left']

    def __init__(self, right:Formula, left:Formula):
        Utils.verified_propositions(right)
        Utils.verified_propositions(left)
        self.__right = right
        self.__left = left 

    def __str__(self):
        return "{} então {}".format(
            self.__right,
            str(self.__left).lower()
        )

    def __repr__(self):
        return "({} -> {})".format(
            repr(self.__right),
            repr(self.__left)
        )

    @property
    def value(self): 
        if self.__right.value == None or self.__left.value == None:
            return 'O valor de algum átomo não foi setado'
        if self.__right.value and not self.__left.value:
            return False 
        else:
            return True

    @value.setter
    def value(self, value):
        print("Não é possivel alterar o valor lógico desta fórmula!")
    
    @value.deleter
    def value(self):
        print("Não é possivel deletar o valor lógico desta fórmula!")

    @property
    def length(self):
        return self.__right.length + self.__left.length + 1

    @length.setter
    def length(self, length):
        print("Não é possivel alterar o tamanho desta fórmula!")
    
    @length.deleter
    def length(self):
        print("Não é possivel deletar o tamanho desta fórmula!")

    @property
    def sub_formula(self):
        set_of_formulas = list(self.__right.sub_formula)
        set_of_formulas += self.__left.sub_formula
        set_of_formulas.append(repr(self))
        return sorted(set(set_of_formulas))

    @sub_formula.setter
    def sub_formula(self, sub_formula):
        print("Não é possivel alterar a sub-fórmula desta fórmula!")

    @sub_formula.deleter
    def sub_formula(self):
        print("Não é possivel deletar a sub-fórmula desta fórmula!")


p = Atom("Está chovendo")
q = Atom("A rua está molhendo")
p.value = True
q.value = False
p_and_q = THEN(p, q)
not_p_and_q = NOT(p_and_q)
print(repr(p_and_q))
print(p_and_q.value)
print(repr(not_p_and_q))
print(not_p_and_q.value)
