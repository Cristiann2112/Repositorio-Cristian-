class Estudiante
__materia = int 


 def __init__(self, cedulaDeIdentidad, Nombre, Apellido):  
        self.cedulaDeIdentidad = cedulaDeIdentidad
        self.nombre = Nombre
        self.apellido = Apellido



      def Inscribirmateria (self): 
           vResult = self.__materia
             print  "El  estudiante", self.nombre+self.apellido +
              "Esta cursando la materia de:", self.__materia)
        return vResult

        def asignarlamateria(self, vMateria): 
        if vMateria < 0:
           
        
        else:
            self.__materia = vMateria
    
       def Retirarmateria (self)
      def Mostrarcursosinscritos (self)    
      print "Cursos Inscritos"
     print materia 

class Egresado(Estudiante):
       #Atributos
     def  Aniodeegreso (self):
          pass
    
class Retirado(Estudiante):
      #Atributos
    def  Fechaderetiro (self):
         pass
 
class Nograduado(Estudiante):
      #Atributos
      def Nograduado (self):
           pass
      def Fechaderetiro (self):
           pass
    


CristianGonzalez = Nograduado("30123456", "Cristian", "Gonzalez")


