import numpy as np 

class SystemOFLineaEquation:
    def __init__(self):
        variable_set = ['x', 'y', 'z', 't', 'p', 'q']
        nVariables = int(input("Enter the number of variables: "))
        self.cols = nVariables+1
        #taking the equations
        nEq = int(input("Enter the number of equations: "))
        self.rows = nEq

        print(f"The variables are x, y, z, t, p, q, from them starting {nVariables} variables will be selected")
        systemOfEq = []
        for i in range(nEq):
            equation = []
            print("Eqaution ", i+1, ": ")
            for j in range(nVariables):
                constantOfVariable = int(input(f"Enter the constant for variable {variable_set[j]}: "))
                equation.append(constantOfVariable)
            equation.append(int(input("The equation equal to: ")))
            systemOfEq.append(equation)
        #This gives me an augmented matrix
        self.system = np.array(systemOfEq)
        if(self.system[:, nVariables].all() == 0):
            print("The system is consistent")
        print(self.system, len(self.system))

    def rowechaelon_conversion(self):
        self.rowechaelon = self.system.copy()
        self.rowechaelon = self.rowechaelon.astype(float)
        pivot = 0
        for i in range(len(self.rowechaelon)):
            if pivot >= self.rowechaelon.shape[1]:
                break
            if self.rowechaelon[i, pivot] != 0:
                for j in range(i+1, len(self.rowechaelon)):
                    if self.rowechaelon[j, pivot] == 0:
                        continue
                    else:
                        mult = self.rowechaelon[j, pivot]/self.rowechaelon[i, pivot]
                        self.rowechaelon[j] -= self.rowechaelon[i] * mult
                pivot += 1
            else:
                #now that the pivot element is zero, we try to swap this row with the one below and move one iteration back
                swapIndex = -1
                for k in range(i+1, len(self.rowechaelon)):
                    if self.rowechaelon[k, pivot] != 0:
                        swapIndex = k
                        break
                    
                if swapIndex != -1:
                    self.rowechaelon[[i, swapIndex]] = self.rowechaelon[[swapIndex, i]]
                    i = i -1
                else:
                    pivot = pivot +1
                    i = i-1
        print("row echaelon: ")
        print(self.rowechaelon)
        pass

    def getRankOfMatrix(self)->int:
        rank1 = 0
        rank2 = 0
        for row in self.rowechaelon[:,0:self.cols]:
            #as given matrix is augmented matrix
            if not np.all(row == 0):
                rank1 += 1

        for row in self.rowechaelon:
            if not np.all(row == 0):
                rank2 += 1

        print("system rank: ", rank1)
        print("Augmented rank: ", rank2)

        if rank1 != rank2:
            print("The system is inconsistent — no solution.")
        elif rank1 == self.system.shape[1] - 1:
            print("Unique solution exists.")
        else:
            print("Infinitely many solutions exist.")
        return 0
    

system1 = SystemOFLineaEquation()
system1.rowechaelon_conversion()
system1.getRankOfMatrix()