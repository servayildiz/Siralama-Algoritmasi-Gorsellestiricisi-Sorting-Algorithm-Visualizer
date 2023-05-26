from tkinter import * 
import tkinter as tk
from tkinter import ttk
import random
import time
# from bubbleSort import * 
# from quickSort import quick_sort
# from insertionSort import insertion_sort
# from mergeSort import merge_sort
# from selectionSort import selection_sort
import matplotlib.pyplot as plt
from celluloid import Camera
from matplotlib.animation import FuncAnimation

ui = '#60A3D9'
button = '#003B73'
bg_light = '#737373'
grad = [
    '#60A3D9',
    '#0074B7'
]
grad = [
    '#60A3D9',
    '#0074B7'
]
grad_green = [
    '#C21010',
    '#E64848'
]

swaps = 0
root = Tk()
style = ttk.Style(root)
root.tk.call("source", "Forest-ttk-theme-master/forest-light.tcl")
ttk.Style().theme_use('forest-light')
root.title('Algorithm Visualisation')
root.maxsize(900, 900)
root.config()
theme_var = StringVar(root)
algo = StringVar
data = []
old_data = []
color=[]

defaultsize = StringVar(root)
defaultsize.set("6")
defaulmin = StringVar(root)
defaulmin.set("0")
defaulmax = StringVar(root)
defaulmax.set("10")
retain = IntVar(root)
fig = plt.figure()
camera = Camera(fig)

sayac = 0

def main():
    global sayac   
    def bubble_sort(data, draw, timeTick):
        global swaps
        global sayac
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                # sayac += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    colors = [grad_green[x % 2] if x == j or x == j + 1 else grad[x % 2] for x in range(len(data))]
                    draw(data, colors, swaps)
                    time.sleep(timeTick)
                    swaps += 1
                    sayac += 1

        draw(data, [grad[x % 2] for x in range(len(data))], swaps)
        label2 = tk.Label(UI_frame, text=str(sayac))
        label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
        swaps = 0
        sayac = 0
        label2 = tk.Label(UI_frame, text=str("0   "))
        # label2.grid(row=4, column=1, padx=0, pady=5, sticky=W)
        return data
    sayac = 0

    # genel complexity : merge sort hariç tüm sıralama algoritmaları için karmaşıklık analizi hesaplar
    def calculate_complexity(data):
        n = len(data)
        complexity = n * (n-1) // 2
        return complexity
    
    # merge sort complexity
    def merge_sort_complexity(arr):
        n = len(arr)
        if n <= 1:
            return 0
        left = arr[:n//2]
        right = arr[n//2:]
        complexity = merge_sort_complexity(left) + merge_sort_complexity(right) + n
        return complexity

    def insertion_sort(data, draw, timeTick):
        global swaps
        global sayac
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
                swaps += 1
                sayac += 1
                colors = [grad_green[x % 2] if x == j + 1 else grad[x % 2] for x in range(len(data))]
                draw(data, colors, swaps)
                time.sleep(timeTick)
            data[j + 1] = key

        draw(data, [grad[x % 2] for x in range(len(data))], swaps)
        label2 = tk.Label(UI_frame, text=str(sayac))
        label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
        swaps = 0
        sayac = 0
        label2 = tk.Label(UI_frame, text=str("0   "))
        # label2.grid(row=4, column=1, padx=0, pady=5, sticky=W)
        return data

    sayac = 0

    
    def merge_sort(data, drawData, timeTick):
        global sayac
        merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


    def merge_sort_alg(data, left, right, drawData, timeTick):
        global sayac
        if left < right:
            middle = (left + right) // 2
            merge_sort_alg(data, left, middle, drawData, timeTick)
            merge_sort_alg(data, middle + 1, right, drawData, timeTick)
            merge(data, left, middle, right, drawData, timeTick)
        if data == sorted(data):
            drawData(data, [grad[x % 2] for x in range(len(data))])
    
    def merge(data, left, middle, right, drawData, timeTick):
        global sayac
        drawData(data, getColorArray(len(data), left, middle, right))
        time.sleep(timeTick)

        leftPart = data[left:middle + 1]
        rightPart = data[middle + 1: right + 1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right + 1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1
                sayac += 1

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(data, [grad_green[0] if x >= left and x <= right else "#CCCCCC" for x in range(len(data))])
        time.sleep(timeTick)
        label2 = tk.Label(UI_frame, text=str(sayac))
        label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
        sayac = 0
        label2 = tk.Label(UI_frame, text=str("0       "))

    def partition(data, head, tail, draw, timeTick):
        global swaps
        global sayac
        border = head
        pivot = data[tail]

        draw(data, getclr(len(data), head, tail, border, border), swaps)
        time.sleep(timeTick)
        for j in range(head, tail):
            if data[j] < pivot:
                draw(data, getclr(len(data), head, tail, border, j, True), swaps)
                time.sleep(timeTick)
                swaps += 1
                sayac += 1
                data[border], data[j] = data[j], data[border]
                border += 1
                time.sleep((timeTick))
            draw(data, getclr(len(data), head, tail, border, j), swaps)
            time.sleep(timeTick)
        # draw(data, [grad_green[0] if x == data[border] or x == data[tail] else grad[x % 2] for x in range(len(data))])
        swaps += 1
        draw(data, getclr(len(data), head, tail, border, tail, True), swaps)
        label2 = tk.Label(UI_frame, text=str(sayac))
        label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
        label2 = tk.Label(UI_frame, text=str("0       "))
        time.sleep(timeTick)
        data[border], data[tail] = data[tail], data[border]
        return border

    def quick_sort(data, head, tail, draw, timeTick):
        global swaps
        global sayac
        if head < tail:
            pi = partition(data, head, tail, draw, timeTick)
            sayac += 1
            quick_sort(data, head, pi - 1, draw, timeTick)
            quick_sort(data, pi + 1, tail, draw, timeTick)

        if data == sorted(data):
            draw(data, [grad[x % 2] for x in range(len(data))], swaps)
            swaps = 0
            sayac += 1

    def getclr(datalen, head, tail, border, currindx, swaping=False):
        colors = []
        for i in range(datalen):
            if head <= i <= tail:
                colors.append(grad[i % 2])
            else:
                colors.append("#CCCCCC")

            if i == tail:
                colors[i] = grad_green[0]
            elif i == border:
                colors[i] = grad_green[1]
            elif i == currindx:
                colors[i] = '#FEC260'

            if swaping:
                if i == border or i == currindx:
                    colors[i] = '#EB1D36'
        return colors

    def getColorArray(leght, left, middle, right):
        colorArray = []

        for i in range(leght):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    colorArray.append(grad[0])
                else:
                    colorArray.append(grad[1])
            else:
                colorArray.append("#CCCCCC")

        return colorArray
    
    def selection_sort(data, draw, timeTick):
        global swaps
        global sayac
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
                sayac += 1
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
                colors = [grad_green[x % 2] if x == i or x == min_index else grad[x % 2] for x in range(len(data))]
                draw(data, colors, swaps)
                time.sleep(timeTick)
                swaps += 1

        draw(data, [grad[x % 2] for x in range(len(data))], swaps)
        swaps = 0
        label2 = tk.Label(UI_frame, text=str(sayac))
        label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
        sayac = 0
        label2 = tk.Label(UI_frame, text=str("0       "))
        return data

    def draw(data, color, swaps=0):
        canvas.delete("all")
        ch = 500
        cw = 810
        xwidth = cw / (len(data) + 1)
        offset = 50
        spacing = 8
        normaldata = [i / max(data) for i in data]

        for i, height in enumerate(normaldata):
            x0 = i * xwidth + offset + spacing
            y0 = ch - height * 440
            x1 = (i + 1) * xwidth + offset
            y1 = ch
            canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], width=0)
            canvas.create_text(x0+59, y1 + 15, text=data[i], fill=color[i], font=('MS Sans Serif', 12))

            # canvas.create_text(100, 100, text=f'SWAPS: {swaps}', fill=grad[1], font=('MS Sans Serif', 12))
        root.update()

    def draw_stem(data, color, swaps=0):
        canvas.delete("all")
        ch = 500
        cw = 810
        xwidth = cw / (len(data) + 1)
        offset = 50
        spacing = 8
        normaldata = [i / max(data) for i in data]


        for i, height in enumerate(normaldata):
            x0 = i * xwidth + offset + spacing
            y0 = ch - height * 440
            x1 = (i + 1) * xwidth + offset
            y1 = ch
            x=int(len(data))
            canvas.create_line(x0 + xwidth / 2, ch, x0 + xwidth / 2, y0, fill=color[i])
            if x==2:
                canvas.create_oval(x0 + 140 , y0 - 5, x0 + 130, y0 + 5, fill=color[i])
            elif x==3:
                canvas.create_oval(x0 + 97 , y0 - 5, x0 + 107, y0 + 5, fill=color[i])
            elif x==4:
                canvas.create_oval(x0 + 76 , y0 - 5, x0 + 86, y0 + 5, fill=color[i])
            elif x==5:
                canvas.create_oval(x0 + 63 , y0 - 5, x0 + 73, y0 + 5, fill=color[i])
            elif x==6:
                canvas.create_oval(x0 + 53 , y0 - 5, x0 + 63, y0 + 5, fill=color[i])
            elif x==7:
                canvas.create_oval(x0 + 46 , y0 - 5, x0 + 56, y0 + 5, fill=color[i])
            elif x==8:
                canvas.create_oval(x0 + 40 , y0 - 5, x0 + 50, y0 + 5, fill=color[i])
            elif x==9:
                canvas.create_oval(x0 + 36 , y0 - 5, x0 + 46, y0 + 5, fill=color[i])
            elif x==10:
                canvas.create_oval(x0 + 32 , y0 - 5, x0 + 42, y0 + 5, fill=color[i])
            elif x==11:
                canvas.create_oval(x0 + 28 , y0 - 5, x0 + 38, y0 + 5, fill=color[i])
            elif x==12:
                canvas.create_oval(x0 + 26 , y0 - 5, x0 + 36, y0 + 5, fill=color[i])
            canvas.create_text(x0+59, y1 + 15, text=data[i], fill=grad[i % 2], font=('MS Sans Serif', 12))
        root.update()

    def draw_scatter(data, color, swaps=0):
        canvas.delete("all")
        ch = 500
        cw = 810
        xwidth = cw / (len(data) + 1)
        offset = 50
        spacing = 8
        normaldata = [i / max(data) for i in data]

        for i, height in enumerate(normaldata):
            x0 = i * xwidth + offset + spacing
            y0 = ch - height * 440
            x1 = (i + 1) * xwidth + offset 
            y1 = ch
            canvas.create_oval(x0 - 5, y0 - 5, x0 + 5, y0 + 5, fill=color[i])
            canvas.create_text(x0, y1 + 15, text=data[i], fill=grad[i % 2], font=('MS Sans Serif', 12))
        root.update()


    # def set_theme():
    #     root.tk.call("set_theme", theme_var.get())

    def generate():
        global data
        # try:
        #     min = int(minEntry.get())
        # except:
        #     min = 1
        # try:
        #     max = int(maxEntry.get())
        # except:
        #     max = 99
        # try:
        #     size = int(sizeEntry.get())
        # except:
        #     size = 60
        data = []

        # if min < 0:
        #     min = 0
        # if max > 500:
        #     max = 500
        # if size > 100:
        #     size = 100
        # if size < 3:
        #     size = 3
        # for _ in range(len(data)):
        data = dataEntry.get()
        data = [int(x.strip()) for x in data.split(",")]

        if graph_option.get() == "Bar Grafiği":
            draw(data, [grad[i % 2] for i in range(len(data))], 0)
        elif graph_option.get() == "Scatter Grafiği":
            draw_scatter(data, [grad[i % 2] for i in range(len(data))], 0)
        elif graph_option.get() == "Stem Grafiği":
            draw_stem(data, [grad[i % 2] for i in range(len(data))], 0)
        # set_theme()

    def startAlgo():
        global data
        global sayac
        if not data:
            return
        
        if algomenu.get() == 'Quick Sort':
            quick_start_time = time.time()
            # quick_sort(data, 0, len(data) - 1, draw, speedScale.get())
            if graph_option.get() == "Bar Grafiği":
                quick_sort(data, 0, len(data) - 1, draw, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Scatter Grafiği":
                quick_sort(data, 0, len(data) - 1, draw_scatter, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Stem Grafiği":
                quick_sort(data, 0, len(data) - 1, draw_stem, speedScale.get())
                complexity = calculate_complexity(data)
                sayac += 1
                label2 = tk.Label(UI_frame, text=str(sayac))
                label2.grid(row=6, column=1, padx=0, pady=5, sticky=W)
            # draw(data, [grad[x % 2] for x in range(len(data))],0)
            quick_end_time = time.time()
            quick_execution_time = quick_end_time - quick_start_time
            label = tk.Label(UI_frame, text=str(complexity))
            label.grid(row=5, column=1, padx=0, pady=5, sticky=W)     
            label3 = tk.Label(UI_frame, text=str(quick_execution_time))
            label3.grid(row=7, column=1, padx=0, pady=5, sticky=W)         

        elif algomenu.get() == 'Bubble Sort':
            bubble_start_time = time.time()
            # bubble_sort(data, draw_scatter, speedScale.get())
            if graph_option.get() == "Bar Grafiği":
                bubble_sort(data, draw, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Scatter Grafiği":
                bubble_sort(data, draw_scatter, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Stem Grafiği":
                bubble_sort(data, draw_stem, speedScale.get())
                complexity = calculate_complexity(data)
            bubble_end_time = time.time()
            bubble_execution_time = bubble_end_time - bubble_start_time
            label = tk.Label(UI_frame, text=str(complexity))
            label.grid(row=5, column=1, padx=0, pady=5, sticky=W)    
            label3 = tk.Label(UI_frame, text=str(bubble_execution_time))
            label3.grid(row=7, column=1, padx=0, pady=5, sticky=W)   

        elif algomenu.get() == 'Merge Sort':
            merge_start_time = time.time()
            # merge_sort(data, draw_stem, speedScale.get())
            if graph_option.get() == "Bar Grafiği":
                merge_sort(data, draw, speedScale.get())
                complexity = merge_sort_complexity(data)
            elif graph_option.get() == "Scatter Grafiği":
                merge_sort(data, draw_scatter, speedScale.get())
                complexity = merge_sort_complexity(data)
            elif graph_option.get() == "Stem Grafiği":
                merge_sort(data, draw_stem, speedScale.get())
                complexity = merge_sort_complexity(data)
            merge_end_time = time.time()
            merge_execution_time = merge_end_time - merge_start_time
            label = tk.Label(UI_frame, text=str(complexity))
            label.grid(row=5, column=1, padx=0, pady=5, sticky=W)
            label3 = tk.Label(UI_frame, text=str(merge_execution_time))
            label3.grid(row=7, column=1, padx=0, pady=5, sticky=W)
            
        elif algomenu.get() == 'Selection Sort':
            selection_start_time = time.time()
            # selection_sort(data, draw, speedScale.get())
            if graph_option.get() == "Bar Grafiği":
                selection_sort(data,  draw, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Scatter Grafiği":
                selection_sort(data,  draw_scatter, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Stem Grafiği":
                selection_sort(data,  draw_stem, speedScale.get())
                complexity = calculate_complexity(data)
            selection_end_time = time.time()
            selection_execution_time = selection_end_time - selection_start_time
            label = tk.Label(UI_frame, text=str(complexity))
            label.grid(row=5, column=1, padx=0, pady=5, sticky=W)    
            label3 = tk.Label(UI_frame, text=str(selection_execution_time))
            label3.grid(row=7, column=1, padx=0, pady=5, sticky=W)            

        elif algomenu.get() == 'Insertion Sort':
            insertion_start_time = time.time()
            # insertion_sort(data, draw, speedScale.get())
            if graph_option.get() == "Bar Grafiği":
                insertion_sort(data,  draw, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Scatter Grafiği":
                insertion_sort(data, draw_scatter, speedScale.get())
                complexity = calculate_complexity(data)
            elif graph_option.get() == "Stem Grafiği":
                insertion_sort(data,  draw_stem, speedScale.get())
                complexity = calculate_complexity(data)
            insertion_end_time = time.time()
            insertion_execution_time = insertion_end_time - insertion_start_time
            label = tk.Label(UI_frame, text=str(complexity))
            label.grid(row=5, column=1, padx=0, pady=5, sticky=W)
            label3 = tk.Label(UI_frame, text=str(insertion_execution_time))
            label3.grid(row=7, column=1, padx=0, pady=5, sticky=W)

    def generate_graph():
        selected_option = graph_option.get()
        if selected_option == "Bar Grafiği":
            draw(data, color)
        elif selected_option == "Scatter Grafiği":
            draw_scatter(data, color)
        elif selected_option == "Stem Grafiği":
            draw_stem(data, color)

    def reset_chart():
       label2 = tk.Label(UI_frame, text=str(0))
       label2.grid(row=5, column=1, padx=0, pady=5, sticky=W)
        # Verileri sıfırla
       data = []

        # Grafik nesnesini sıfırla
       fig.clear()

        # Canvas'ı temizle
       canvas.delete("all")

        # Canvas'ı güncelle
       canvas.draw()

    def stop_animation():
        global camera
        # plt.pause(0.01)
        # # Animasyonu durdur
        # camera.stop()
    
        # # Kamera nesnesini sıfırla
        camera = Camera(fig)
        # controller = AnimationController()
        camera.snap()
        # global ani

        # Animasyonu durdur
        # camera.event_source.stop()


    UI_frame = ttk.Frame(root, width=900, height=50)
    UI_frame.pack(padx=0, pady=0, side=TOP)

    canvas = Canvas(root, width=1100, height=800)
    canvas.pack(side=BOTTOM)

    Label(UI_frame, text="Sıralama Algoritması: ").grid(row=0, column=0, padx=0, pady=5, sticky=W)
    algomenu = ttk.Combobox(UI_frame, textvariable=algo,
                            values=['Bubble Sort', 'Quick Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort'])
    algomenu.grid(row=0, column=1, padx=13, pady=5)
    algomenu.current(0)

    Label(UI_frame, text="Grafik Tipi: ").grid(row=1, column=0, padx=0, pady=5, sticky=W)
    graph_options = ['Bar Grafiği', 'Scatter Grafiği', 'Stem Grafiği']
    graph_option = ttk.Combobox(UI_frame, values=graph_options)
    graph_option.grid(row=1, column=1, padx=10, pady=5)
    graph_option.current(0)

    ttk.Button(
        UI_frame, text="Başla", style="Accent.TButton", command=startAlgo
    ).grid(row=2, column=3, padx=13, pady=0)

    reset_button = ttk.Button(UI_frame, text="Sıfırla", style="Accent.TButton", command=reset_chart)
    reset_button.grid(row=3, column=3, padx=10, pady=5)

    ttk.Button(
        UI_frame, text="Oluştur", style="Accent.TButton", command=generate
    ).grid(row=1, column=3, padx=0, pady=6)
    ttk.Button(
        UI_frame, text="Dur", style="Accent.TButton", command=stop_animation
    ).grid(row=4, column=3, padx=13, pady=0)


    Label(UI_frame, text="Veriler: ").grid(row=2, column=0, padx=0, pady=5, sticky=W)
    dataEntry = ttk.Entry(UI_frame, width=15)
    dataEntry.grid(row=2, column=1, padx=13, pady=5, sticky=W) 

    Label(UI_frame, text="Hız: ").grid(row=3, column=0, padx=0, pady=5, sticky=W)
    speedScale = ttk.Scale(UI_frame, from_=1, to_=0.000001, length=150)
    speedScale.set(0.25)
    speedScale.grid(row=4, column=0, padx=13)


    Label(UI_frame, text="Karmaşıklık Analizi O(n): ").grid(row=5, column=0, padx=0, pady=5, sticky=W)

    Label(UI_frame, text="Karşılaştırma Sayısı: ").grid(row=6, column=0, padx=0, pady=5, sticky=W)

    Label(UI_frame, text="Gerçekleşme Süresi: ").grid(row=7, column=0, padx=0, pady=5, sticky=W)

    root.mainloop()
            
if __name__ == "__main__":
    main()
