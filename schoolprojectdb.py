from mysql.connector import connect, Error

class School:

    def __init__(self,studentNumber=None,name=None,surname=None,birthDate=None,gender=None,classId=None,branch=None,id=None):
        self.connection = connect(
            host="localhost",
            user="root",
            password="password",
            database="schoolprojectdb"
        )
        self.cursor = self.connection.cursor()
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        self.gender = gender
        self.classId = classId
        self.branch = branch
        self.id=id

    # Students
    def getStudents(self):
        sql = "SELECT student.studentNumber,student.name,student.surname,student.birthDate,class.name FROM student INNER JOIN class ON class.id=student.classId"
        self.cursor.execute(sql)
        try:
            for i in self.cursor.fetchall():
                print(f"*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nNumara: {i[0]}\nAd: {i[1]}\nSoyad: {i[2]}\nDoğum Tarihi: {i[3]}\nSınıfı: {i[4]}")
        except Error as err:
            print("Hata:",err)
        finally:
            self.connection.close()

    def addStudent(self):
        sql = "INSERT INTO student(studentNumber,name,surname,birthDate,gender,classId) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (self.studentNumber,self.name,self.surname,self.birthDate,self.gender,self.classId)
        try:
            self.cursor.execute(sql,values)
            self.connection.commit()
            print("Kayıt Eklendi!")
        except Error as err:
            print("Hata: ",err)
        finally:
            self.connection.close()

    def updateStudent(self):
        sql = "UPDATE student SET classId=%s WHERE studentNumber=%s"
        values = (self.classId,self.studentNumber)
        try:
            self.cursor.execute(sql,values)
            self.connection.commit()
            print("Kayıt Güncellendi!")
        except Error as err:
            print("Hata: ", err)
        finally:
            self.connection.close()

    def deleteStudent(self):
        sql = "DELETE FROM student WHERE studentNumber=%s"
        values=(self.studentNumber,)
        try:
            self.cursor.execute(sql,values)
            self.connection.commit()
            print("Kayıt Silindi!")
        except Error as err:
            print("Hata: ", err)
        finally:
            self.connection.close()

    # Teachers
    def getTeachers(self):
        sql = "SELECT branch,name,surname,birthDate,id FROM teacher"
        self.cursor.execute(sql)
        try:
            for i in self.cursor.fetchall():
                print(f"*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\nKayıt Numarası: {i[-1]}\nAd: {i[1]}\nSoyad: {i[2]}\nBranş: {i[0]}\nDoğum Tarihi: {i[3]}")
        except Error as err:
            print("Hata: ",err)
        finally:
            self.connection.close()

    def addTeacher(self):
        sql = "INSERT INTO teacher(branch,name,surname,birthDate,gender) VALUES(%s,%s,%s,%s,%s)"
        values = (self.branch,self.name,self.surname,self.birthDate,self.gender)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Bir Kayıt Eklendi!")
        except Error as err:
            print("Hata: ",err)
        finally:
            self.connection.close()

    def updateTeacher(self):
        sql = "UPDATE teacher SET branch=%s WHERE id=%s"
        values = (self.branch,self.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Bir Kayıt Güncellendi!")
        except Error as err:
            print("Hata: ",err)
        finally:
            self.connection.close()

    def deleteTeacher(self):
        sql = "DELETE FROM teacher WHERE id=%s"
        values = (self.id,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print("Bir Kayıt Silindi!")
        except Error as err:
            print("Hata: ",err)
        finally:
            self.connection.close()

    def __del__(self):
        self.connection.close()
        print("Database bağlantısı kesildi!")

while True:
    islem = input("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n--Öğrenci İşlemleri--\n-----1) Öğrencileri Göster\n-----2) Öğrenci Ekle\n-----3) Öğrenci Güncelle\n-----4) Öğrenci Sil\n**********************"
                  "\n--Öğretmen İşlemleri--\n-----5) Öğretmenleri Göster\n-----6) Öğretmen Ekle\n-----7) Öğretmen Güncelle\n-----8) Öğretmen Sil\n0) Çıkış\nİşlem Numarası: ")
    if islem == "0":
        break
    else:
        if islem == "1":
            school = School()
            school.getStudents()
        elif islem == "2":
            studentNumber = input("Öğrenci Numarası: ")
            name = input("Ad: ")
            surname = input("Soyad: ")
            birthDate = input("Doğum Tarihi: ")
            gender = input("Cinsiyet: ")
            classId = input("Sınıf Numarası: ")
            school = School(studentNumber,name,surname,birthDate,gender,classId)
            school.addStudent()
        elif islem == "3":
            studentNumber = input("Sınıfını güncellemek istediğiniz Öğrencinin Numarası: ")
            classId = input("Öğrencinin aktarılacağı Sınıf Numarası: ")
            school = School(studentNumber=studentNumber,classId=classId)
            school.updateStudent()
        elif islem == "4":
            studentNumber = input("Silmek istediğiniz Öğrencinin Numarası: ")
            school = School(studentNumber=studentNumber)
            school.deleteStudent()
        elif islem == "5":
            school = School()
            school.getTeachers()
        elif islem == "6":
            branch = input("Branş: ")
            name = input("Ad: ")
            surname = input("Soyad: ")
            birthDate = input("Doğum Tarihi: ")
            gender = input("Cinsiyet: ")
            school = School(branch=branch,name=name,surname=surname,birthDate=birthDate,gender=gender)
            school.addTeacher()
        elif islem == "7":
            id = input("Branşını güncellemek istediğiniz Öğretmenin Kayıt Numarası")
            branch = input("Öğretmenin yeni Branşı: ")
            school = School(id=id,branch=branch)
            school.updateTeacher()
        elif islem == "8":
            id = input("Silmek istediğiniz Öğretmenin Kayıt Numarası: ")
            school = School(id=id)
            school.deleteTeacher()
