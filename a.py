from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Variavel global que define o tipo de projecao
op = 0
# Variavel global que define o incremento
increment = 3.47
# Variavel global que define a escala
zoom = 1
# Variaveis globais que definem os angulos de rotacao nos eixos x, y e z
angle_x = 0
angle_y = 0
angle_z = 0
# Variaveis globais que definem as posicoes de translacao nos eixos x, y e z
pos_x = 0
pos_y = 0
pos_z = 0


def init():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE)
	glutInitWindowSize(700, 700)
	glutCreateWindow("Teapot")

	glClearColor(1, 1, 1, 0)


def setProjection(mask):
	# Define que ira trabalhar com a matriz de projecao
	glMatrixMode(GL_PROJECTION)
	# Carrega a matriz identidade
	glLoadIdentity()

	# Projecao ortogonal
	if (op == 0):
		# x_min, x_max, y_min, y_max, z_min, z_max 
		glOrtho(20 if (mask & 1) else -20, -20 if (mask & 1) else 20, 
				20 if (mask & 2) else -20, -20 if (mask & 2) else 20, -200, 200)
	# Projecao perspectiva
	else:
		# x_min, x_max, y_min, y_max, z_near, z_far
		glFrustum(10 if (mask & 1) else -10, -10 if (mask & 1) else 10, 
				10 if (mask & 2) else -10, -10 if (mask & 2) else 10, 10, 200)


# Desenha os eixos x, y e z em degrade
def drawAxis() :
	# Eixo x -> vermelho
	glBegin(GL_LINES)
	glColor3f(1, 0, 0)
	glVertex3f(0,0,0)
	glVertex3f(40,0,0)
	glEnd()
	
	# Eixo y -> amarelo
	glBegin(GL_LINES)
	glColor3f(1, 1, 0)
	glVertex3f(0,0,0)
	glVertex3f(0,40,0)
	glEnd()

	# Eixo z -> azul
	glBegin(GL_LINES)
	glColor3f(0, 0, 1)
	glVertex3f(0,0,0)
	glVertex3f(0,0,40)
	glEnd()

	
# Funcao para capturar os eventos do teclado
def keyPressEvent(key, x, y) :
	global angle_x, angle_y, angle_z, increment, pos_x, pos_y, pos_z, zoom

	if key == '\x1b':
		exit(0) # Sai do programa se apertar ESC
	
	if (key == 'Q'):
		angle_x += increment # Rotaciona em x no sentido anti horario
	elif (key == 'A'):
		angle_x -= increment # Rotaciona em x no sentido horario
	elif (key == 'W'):
		angle_y += increment # Rotaciona em y no sentido anti horario
	elif (key == 'S'):
		angle_y -= increment # Rotaciona em y no sentido horario
	elif (key == 'E'):
		angle_z += increment # Rotaciona em z no sentido anti horario
	elif (key == 'D'):
		angle_z -= increment # Rotaciona em z no sentido horario
	else: 
		pass
	
	if (key == 'q'):
		pos_x += increment # Translada em x no sentido positivo
	elif (key == 'a'):
		pos_x -= increment # Translada em x no sentido negativo
	elif (key == 'w'):
		pos_y += increment # Translada em y no sentido positivo
	elif (key == 's'):
		pos_y -= increment # Translada em y no sentido negativo
	elif (key == 'e'):
		pos_z += increment # Translada em z no sentido positivo
	elif (key == 'd'):
		pos_z -= increment # Translada em z no sentido negativo
	else: 
		pass

	if (key == '+'):
		zoom += 0.1 # Aumenta a escala
	elif (key == '-'):
		zoom -= 0.1 # Diminui a escala
	else:
		pass

	display()


def displayViewPort(x, y, w, h, mask):
	global pos_x, pos_y, pos_z
	global angle_x, angle_y, angle_z, zoom

	# Define uma porta de visao para a projecao ortogonal
	glViewport(x, y, w, h)

	# Chama a funcao para configurar o tipo de projecao ortogonal
	setProjection(mask)

	# Define as configuracoes do observador
	gluLookAt(15, 15, 15, 0, 0, 0, 0, 1, 0)

	# Define que ira trabalhar com a matriz de modelo/visao
	glMatrixMode(GL_MODELVIEW)

	# Carrega a matriz identidade
	glLoadIdentity()

	# Desenha os eixos 
	drawAxis()

	# Translada o objeto
	glTranslatef(pos_x, pos_y, pos_z)

	# Rotaciona o objeto
	glRotatef(angle_x, 1, 0, 0)
	glRotatef(angle_y, 0, 1, 0)
	glRotatef(angle_z, 0, 0, 1)

	# Escala o objeto
	glScalef(zoom, zoom, zoom)

	# Desenha um bule de arame na cor verde
	glColor3f(0,1,0)
	glutWireTeapot(10.0)


def drawLines():
	glViewport(0, 0, 700, 700)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-0.50, 700, -0.5, 700, -1, 1)

	#Vertical 
	glBegin(GL_LINES)
	glColor3f(0.6, 0.6, 0.6)
	glVertex3f(350, 0, 0)
	glVertex3f(350, 700, 0)
	glEnd()

	#Horizontal
	glBegin(GL_LINES)
	glColor3f(0.6, 0.6, 0.6)
	glVertex3f(0,350,0)
	glVertex3f(700,350,0)
	glEnd()

	
def display():

	glClear(GL_COLOR_BUFFER_BIT)

	displayViewPort(0, 350, 350, 350, 0);
	displayViewPort(350, 350, 350, 350, 1); # Espelha no eixo x
	displayViewPort(0, 0, 350, 350, 2); # Espelha no eixo y
	displayViewPort(350, 0, 350, 350, 3); # Espelha nos eixos x e y
	drawLines()

	glutSwapBuffers()


op = input("Qual o tipo de projecao desejada? Digite 0 para paralela e 1 para perspectiva: ")

print("\nINFORMACOES")
print("===========\n")
print("\tO eixo vermelho e o eixo x")
print("\tO eixo amarelo e o eixo y")
print("\tO eixo azul e o eixo z\n")

print("COMANDOS")
print("========\n")
print("\tTRANSLACAO")
print("\t\t(q) --> positiva no eixo x")
print("\t\t(a) --> negativa no eixo x")
print("\t\t(w) --> positiva no eixo y")
print("\t\t(s) --> negativa no eixo y")
print("\t\t(e) --> positiva no eixo z")
print("\t\t(d) --> negativa no eixo z\n")
print("\tROTACAO")
print("\t\t(Q) (shift + q) --> sentido anti horario no eixo x")
print("\t\t(A) (shift + a) --> sentido horario no eixo x")
print("\t\t(W) (shift + w) --> sentido anti horario no eixo y")
print("\t\t(S) (shift + s) --> sentido horario no eixo y")
print("\t\t(E) (shift + e) --> sentido anti horario no eixo z")
print("\t\t(D) (shift + d) --> sentido horario no eixo z\n")
print("\tESCALA")
print("\t\t(+) (shift + =) --> aumenta a escala")
print("\t\t(-) --> diminui a escala\n")

raw_input("Pressione ENTER para continuar")

init()
glutDisplayFunc(display)
glutKeyboardFunc(keyPressEvent)

glutMainLoop()