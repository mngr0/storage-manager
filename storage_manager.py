from RPi import GPIO


class StorageManager:
   
    
    def read_storage_state(self):
        f = open ("storage_state","r")
        for level in self.storage:
            for slot in level:
                slot= f.readline()
    
    def __init__(self):
 

        n_levels = 10
        slot_per_level = 6
        storage =[]

for l in range(n_levels):
    storage.append([])
    for s in range(slot_per_level):
        storage[-1].append(None)

       self.LED_MATRIX=[[0,1,2,3,4],[5,6,7,8,9]]
        self.BUTTON_MATRIX=[[10,11,12,13,14],[15,16,17,18,19]]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_MATRIX[0],GPIO.OUT)
        GPIO.setup(LED_MATRIX[1],GPIO.OUT)
        GPIO.setup(BUTTON_MATRIX[0],GPIO.IN)
        GPIO.setup(BUTTON_MATRIX[1],GPIO.IN)
        GPIO.output(LED_MATRIX[0],0)
        GPIO.output(LED_MATRIX[0],0)
        actual_y = 0

        actual_x = None

        self.read_storage_state()
        
        f = open ("position_x" , "r")
        self.ctual_x = int(f.readline())
        move_to(0,None)



def read_storage_state():
    pass



def move_to(x,y):
    #rotate to x
    #switch on y
    GPIO.output(LED_MATRIX[0][actual_y/5],0)
    GPIO.output(LED_MATRIX[1][actual_y%5],0)
    GPIO.output(LED_MATRIX[0][y/5],1)
    GPIO.output(LED_MATRIX[1][y%5],1)
    
    actual_x = x
    actual_y = y
    #write to file last x    
    f = open("position_x", "w")
    f.write(str(actual_x))

def set_storage_place(value,package):
    side_x = None
    side_y = None
    for x, ch_x in enumerate(BUTTON_MATRIX[0]):
        if GPIO.input(ch_x):
            side_x = x

    for y, ch_y in enumerate(BUTTON_MATRIX[1]):
        if GPIO.input(ch_y):
            side_y = y

    if side_x is not None and side_y is not None:
        slot = side_y * 5 + side_x
        #storage[slot/n_level][0]


    ####### re try without buttons
    if storage[actual_y][actual_x] is None:
        storage[actual_y][actual_x] = (value,package)

    #rewrite file
    f = open ("storage_state","w")
    for level in storage:
        for slot in level:
            f.write(str(slot))

def show_storage_place(value,package):
    found = None
    for x,level in enumerate(storage):
        for y,slot in enumerate(level):
            if slot == (value, package):
                found = (x,y)
                break
    if found is not None:
        move_to(found[0],found[1])
    else:
        move_to(actual_x, -1)
