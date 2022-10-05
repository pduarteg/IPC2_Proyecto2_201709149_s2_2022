import Lector as LectorClass
import Escritor as WriterClass

import Lista_clientes
import Cliente
import Simulator

import sys
from tkinter import filedialog
from tkinter import *
import re
import os

class Menu:

    reader_obj = LectorClass.Lector()
    escritor_obj = WriterClass.Escritor()
    sim_obj = Simulator.Simulator()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ╔═══════════════════════════════════════════════════════════════════════════╗")
        print(" ║                        M E N Ú   P R I N C I P A L                        ║")
        print(" ╚═══════════════════════════════════════════════════════════════════════════╝")
        print("")
        print("     [1] Configuración de empresas.")
        print("     [2] Selección de empresa y punto de atención.")
        print("     [3] Manejo de puntos de atención.")
        print("     [4] Visualizar estructuras.")
        print("     [6] Salir.")
        print("")
        print(" Escriba el número de acuerdo a la opción que desee: ")

    def print_submenu_1(self):
        print("")
        print("     ¯¨'*•~-.¸¸,.-~*'[ Configuración de Empresas ]¯¨'*•~-.¸¸,.-~*'")        
        print("")
        print(" [1] Cargar archivo de configuración del sistema.")        
        print(" [2] Cargar archivo de configuración inicial.")
        print(" [3] Crear nueva empresa.") 
        print(" [4] Aplicar una configuración.")       
        print(" [5] Limpiar sistema.")
        print(" [6] Volver al menú principal.")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")
        print("")

        submenu_option_1 = 0
        try:
            submenu_option_1 = int(input())
        except:
            print("Opción no válida.")
            submenu_option_1 = 0

        if submenu_option_1 == 1:            
            print(" - Elija el archivo para cargarlo:")

            if self.reader_obj.open_a_file():
                if self.reader_obj.read_file():
                    print(" *** Carga realizada exitosamente.")
                    print("")
                    self.reader_obj.proces_file_1()                
        elif submenu_option_1 == 2: # CARGA DE ARCHIVO 2
            print(" - Elija el archivo para cargarlo:")

            if self.reader_obj.open_a_file():
                if self.reader_obj.read_file():
                    print(" *** Carga realizada exitosamente.")
                    print("")
                    self.reader_obj.proces_file_2()            
        elif submenu_option_1 == 3: # Creación de empresa (manual)
            print("")
            print("     ¯¨'*•~-.¸¸,.-~*'[ Creación de empresa ]¯¨'*•~-.¸¸,.-~*'")
            print("")
        elif submenu_option_1 == 4: # Aplicación de configuraciones.
            print("")
            print("     ¯¨'*•~-.¸¸,.-~*'[ Aplicación de Configuraciones ]¯¨'*•~-.¸¸,.-~*'")
            print("")
            if self.reader_obj.saved_settings != None:
                self.mostrar_conf_disponibles()
            else:
                print(" (!) No se han cargado configuraciones.")
                print("")
            
        elif submenu_option_1 == 5: # Limpieza de las estructuras
            print(" *** Se limpiará el sistema de evaluación actual...")            
            self.sim_obj.reset_all()
            print(" *** Datos reiniciados.")
            print("")
        elif submenu_option_1 == 6: # Volver a menú principal.
            print(" Volviendo al menú principal...")
            print("")
 
    def mostrar_empresas_disponibles(self):        
        while True:
            n = 1
            temp = self.reader_obj.list_of_processed_companies.first
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1
            print(" [0] Volver sin seleccionar")

            print("")
            print("Escriba el número correspondiente a la empresa para realizar la prueba:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print("Opción no válida, ingrese un número.")
                continue

            total_companies = self.reader_obj.list_of_processed_companies.cant
            if p_option <= total_companies and p_option != 0:
                p_selected = self.reader_obj.list_of_processed_companies.buscar_por_posicion(p_option)
                print("Se ha seleccionado a la empresa:")
                p_selected.imprimir_datos_de_empresa()

                self.sim_obj.to_test_company = p_selected
                print("")
                self.mostrar_puntos_disponibles(p_selected)
                print("")
            elif p_option == 0:
                print(" Volviendo al menú principal...")
                break
            break

    def mostrar_puntos_disponibles(self, company):
        while True:
            n = 1
            temp = company.point_list.first
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.name)
                temp = temp.next
                n += 1

            print("")
            print("Escriba el número correspondiente al punto para realizar la prueba:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print(" (!) Opción no válida, ingrese un número.")
                continue

            total_points = company.point_list.cant
            if p_option <= total_points:
                p_selected = company.point_list.buscar_por_posicion(p_option)
                print(" *** Se ha seleccionado al punto:")
                p_selected.imprimir_datos_de_punto()

                self.sim_obj.to_test_point = p_selected
                print("")
                print(" *** Preparación para prueba completada.")
                print("")
            break

    def mostrar_conf_disponibles(self):        
        while True:
            n = 1
            temp = self.reader_obj.saved_settings.first
            
            while temp != None:
                print(" [" + str(n) + "] " + temp.id)
                temp = temp.next
                n += 1
            print(" [0] Volver sin seleccionar")

            print("")
            print("Escriba el número correspondiente a la configuración para aplicar:")

            p_option = 0
            try:
                p_option = int(input())
            except:
                print("Opción no válida, ingrese un número.")
                continue

            total_settings = self.reader_obj.saved_settings.cant
            if p_option <= total_settings and p_option != 0:
                p_selected = self.reader_obj.saved_settings.buscar_por_posicion(p_option)
                print(" *** Se ha seleccionado a la configuración:")
                print("     ID: " + p_selected.id)
                data = self.reader_obj.list_of_processed_companies
                p_selected.apply(data)
                self.sim_obj.to_test_setting = p_selected
                print("")
            elif p_option == 0:
                print(" Volviendo al menú principal...")
                break
            break

    def iniciar_menu(self):
        print("")
        while(self.exit == False):
            self.imprimir_menu()
            try:
                selected_option = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")
                continue

            if selected_option == 1:
                self.print_submenu_1()
            elif selected_option == 2: # Selección de empresa y punto de atención
                print("")
                print("     ¯¨'*•~-.¸¸,.-~*'[ Selección de Empresa y Punto de Atención ]¯¨'*•~-.¸¸,.-~*'")
                print("")
                if self.reader_obj.list_of_processed_companies != None:
                    self.mostrar_empresas_disponibles()
                else:
                    print(" (!) No se han cargado empresas.")
                    print("")

            elif selected_option == 3:
                print("")
                print("     ¯¨'*•~-.¸¸,.-~*'[ Manejo de Puntos de Atención ]¯¨'*•~-.¸¸,.-~*'")
                print("")
                print(" [1] Ver estado del punto de atención.")
                print(" [2] Activar escritorio de servicio.")
                print(" [3] Desactivar escritorio.")
                print(" [4] Atender cliente.")
                print(" [5] Solicitud de atención.")
                print(" [6] Simular actividad del punto de atención.")
                print("")
                print(" Escriba el número de acuerdo a la opción que desee: ")

                submenu_selected_option_3 = 0

                try:
                    submenu_selected_option_3 = int(input())
                except:
                    print(" *** Error de entrada, debe ingresar un número.")
                    submenu_selected_option_3 = 0

                if submenu_selected_option_3 == 1:
                    print("submenu 3 opción 1")
                    if self.sim_obj.to_test_company != None and self.sim_obj.to_test_point != None:
                        if self.sim_obj.to_test_setting != None and self.sim_obj.test_initialized:
                            print("     ¯¨'*•~-.¸¸,.-~*'[ Estado del punto de atención ]¯¨'*•~-.¸¸,.-~*'")
                            print("")

                            # Estado del punto de atención
                            print(" Punto de simulación actual: ")
                            self.sim_obj.to_test_point.imprimir_datos_de_punto()
                            print("")
                            self.sim_obj.to_test_point.desk_list.contar_todos()
                            active_n = self.sim_obj.to_test_point.desk_list.active_n
                            unactive_n = self.sim_obj.to_test_point.desk_list.unactive_n
                            print(" Cantidad de escritorios de servicio activos: " + str(active_n))
                            print(" Cantidad de escritorios de servicio inactivos: " + str(unactive_n))
                            
                            if self.sim_obj.to_test_client_list.cant != 0:
                                print(" Clientes en espera: ")
                                print("")
                                t = self.sim_obj.to_test_client_list.first
                                while t != None:
                                    print("     - Nombre: " + t.name + ", DPI: " + t.dpi)
                                    t = t.next
                            else:
                                print(" Sin clientes en espera.")
                            
                            print("")
                            print(" Estado de los escritorios:")
                            print("")

                            # Estado del escritorio
                            temp = self.sim_obj.to_test_point.desk_list.first
                            while temp != None:
                                if temp.state:
                                    temp.print_desk_state()
                                temp = temp.next
                            print("")
                        else:
                            print(" (!) No se ha iniciado una simulación.")
                            print("")
                    else:
                        print(" *** No se ha seleccionado una empresa y punto de atención para realizar las pruebas.")
                        print("")

                elif submenu_selected_option_3 == 2: # Activar escritorio
                    if self.sim_obj.to_test_company != None and self.sim_obj.to_test_point != None:
                        print(" --- Escritorios inactivos actualmente:")
                        print("")
                        list = self.sim_obj.to_test_point.desk_list
                        list.mostrar_inactivos()                        
                        print("")
                        print(" - Escriba el número correspondiente al escritorio para activar:")

                        selected_desk = 0
                        try:
                            selected_desk = int(input())
                        except:
                            print(" (!) Opción no válida.")
                            selected_desk = 0

                        list.contar_todos()
                        unactive_n = list.unactive_n

                        if selected_desk > 0 and selected_desk <= unactive_n:
                            desk_to_active = list.buscar_inactivo(selected_desk)
                            if desk_to_active != None:
                                desk_to_active.set_state(True)
                            else:
                                print("Ha ocurrido un error en la activación.")
                            print("")
                        elif selected_desk == 0:
                            print("")
                        else:
                            print(" (!) Opción fuera de rango.")
                            print("")
                    else:
                        print(" *** No se ha seleccionado una empresa y punto de atención para realizar las pruebas.")
                        print("")
                elif submenu_selected_option_3 == 3: # Desactivar escritorio
                    if self.sim_obj.to_test_company != None and self.sim_obj.to_test_point != None:
                        print(" --- Escritorios activos actualmente:")
                        print("")
                        list = self.sim_obj.to_test_point.desk_list
                        list.mostrar_activos()                        
                        print("")
                        print(" - Escriba el número correspondiente al escritorio para desactivar:")

                        selected_desk = 0
                        try:
                            selected_desk = int(input())
                        except:
                            print(" (!) Opción no válida.")
                            selected_desk = 0

                        list.contar_todos()
                        active_n = list.active_n

                        if selected_desk > 0 and selected_desk <= active_n:
                            desk_to_deactive = list.buscar_activo(selected_desk)
                            if desk_to_deactive != None:
                                desk_to_deactive.set_state(False)
                            else:
                                print("Ha ocurrido un error en la desactivación.")
                            print("")
                        elif selected_desk == 0:
                            print("")
                        else:
                            print(" (!) Opción fuera de rango.")
                            print("")
                    else:
                        print(" *** No se ha seleccionado una empresa y punto de atención para realizar las pruebas.")
                        print("")
                elif submenu_selected_option_3 == 4:
                    if self.sim_obj.test_initialized:
                        if self.sim_obj.to_test_client_list.first != None:
                            print(" *** Atendiendo clientes en cola...")
                            self.sim_obj.finish_service()
                        else:
                            print(" *** No hay clientes por atender.")
                    else:
                        print(" (!) No se ha iniciado una simulación.")
                elif submenu_selected_option_3 == 5:
                    if self.sim_obj.test_initialized:
                        print("     ¯¨'*•~-.¸¸,.-~*'[ Solicitud de atención ]¯¨'*•~-.¸¸,.-~*'")
                        self.sim_obj.request_service()
                    else:
                        print(" (!) No se ha iniciado una simulación.")
                        print("")
                elif submenu_selected_option_3 == 6:
                    if self.sim_obj.to_test_setting != None:
                        print(" *** Inicializando la simulación...")                        
                        self.sim_obj.initialize_test()
                        print(" *** Simulación inicializada.")
                        print("")
                    else:
                        print(" (!) No se ha aplicado una configuración inicial.")
                        print("")
            elif selected_option == 4:
                print("menu 4")
            elif selected_option == 5:
                print("menu 5")
            elif selected_option == 6:
                self.exit = True
                print("")
                print("Se cerrará el programa.")
                print(". . .")
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")