from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Variavel global que define o incremento
increment = 3.47
# Variavel global que define o tipo de projecao
op = 0
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
	glutInitWindowSize(500, 500)
	glutCreateWindow("Teapot")

	glClearColor(1, 1, 1, 0)

def setProjection():
	# Define que ira trabalhar com a matriz de projecao
	glMatrixMode(GL_PROJECTION)
	# Carrega a matriz identidade
	glLoadIdentity()

	# Projecao ortogonal
	if (op == 0):
		# x_min, x_max, y_min, y_max, z_min, z_max 
		glOrtho(-20, 20, -20, 20, -200, 200)
	# Projecao perspectiva
	else:
		# x_min, x_max, y_min, y_max, z_near, z_far
		glFrustum(-0.5, 0.5, -0.5, 0.5, 0.5, 50)

# Desenha os eixos x, y e z em degrade
def drawAxis() :
	# Eixo x -> vermelho
	glBegin(GL_LINES)
	glColor3f(1, 0, 0)
	glVertex3f(0,0,0)
	glColor3f(1, 1, 1)
	glVertex3f(20,0,0)
	glEnd()
	
	# Eixo y -> amarelo
	glColor3f(1, 1, 0)
	glBegin(GL_LINES)
	glVertex3f(0,0,0)
	glColor3f(1, 1, 1)
	glVertex3f(0,20,0)
	glEnd()

	# Eixo z -> azul
	glColor3f(0, 0, 1)
	glBegin(GL_LINES)
	glVertex3f(0,0,0)
	glColor3f(1, 1, 1)
	glVertex3f(0,0,20)
	glEnd()
	
# Funcao para capturar os eventos do teclado
def keyPressEvent(key, x, y) :
	global angle_x, angle_y, angle_z, increment, pos_x, pos_y, pos_z

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
		pos_x += increment # Rotaciona em x no sentido anti horario
	elif (key == 'a'):
		pos_x -= increment # Rotaciona em x no sentido horario
	elif (key == 'w'):
		pos_y += increment # Rotaciona em y no sentido anti horario
	elif (key == 's'):
		pos_y -= increment # Rotaciona em y no sentido horario
	elif (key == 'e'):
		pos_z += increment # Rotaciona em z no sentido anti horario
	elif (key == 'd'):
		pos_z -= increment # Rotaciona em z no sentido horario
	else: 
		pass

	display()

def display():
	glClear(GL_COLOR_BUFFER_BIT)

	# Define uma porta de visao para a projecao ortogonal
	glViewport(0, 0, 500, 500)

	# Chama a funcao para configurar o tipo de projecao ortogonal
	setProjection()

	# Define que ira trabalhar com a matriz de modelo/visao
	glMatrixMode(GL_MODELVIEW)

	# Carrega a matriz identidade
	glLoadIdentity()
	
	# Define as configuracoes do observador
	gluLookAt(2, 2, 2, 0, 0, 0, 0, 1, 0)
	
	
# Desenha os eixos 
	drawAxis()
	# Rotaciona o objeto
	global pos_x, pos_y, pos_z
	global angle_x, angle_y, angle_z
	
	glTranslatef(0, 0, 0)
	glRotatef(angle_x, 1, 0, 0)
	glRotatef(angle_y, 0, 1, 0)
	glRotatef(angle_z, 0, 0, 1)
	#glTranslatef(pos_x, pos_y, pos_z)


	# Translada o objeto
	glTranslatef(pos_x, pos_y, pos_z)

	# Desenha um bule de arame na cor verde
	glColor3f(0,1,0)
	glutWireTeapot(10.0)

	glFlush()


print("Qual o tipo de projecao desejada?")
print("Digite 0 para paralela e 1 para perspectiva")
op = input()

init()
glutDisplayFunc(display)
glutKeyboardFunc(keyPressEvent)

glutMainLoop()