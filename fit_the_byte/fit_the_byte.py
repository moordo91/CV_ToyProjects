import cv2 as cv
import tkinter as tk
from tkinter import messagebox
import os

def exchange_byte(target_byte: str) -> int:
    tokens = target_byte.split(' ')
    if tokens[1] in ['mb', 'MB', 'Mb']:
        return int(tokens[0]) * 10**6
    elif tokens[1] in ['kb', 'KB', 'Kb']:
        return int(tokens[0]) * 10**3
    else:
        return int(tokens[0])
    

def fit_the_byte(file_name: str, target_byte: str):
    img = cv.imread(f"./{file_name}")
    file_byte = os.path.getsize(f'./{file_name}')
    target_byte = exchange_byte(target_byte)
    
    if file_byte <= target_byte:
        print("You don't need resize the image...")
        
    scale = target_byte / file_byte
    h, w, *_ = img.shape
    
    resized_img = cv.resize(img, (int(w * scale), int(h * scale)))
    
    return resized_img


if __name__ == '__main__':
    
    file_name = input("Input File Name(ex. image.jpg): ")
    target_byte = input("Input Target Byte(ex. 2.0 MB): ")
    
    try:
        resized_img = fit_the_byte(file_name, target_byte)
        
        cv.imshow('Resized Image', resized_img)
        
        key = cv.waitKey()
        if key == 27:    
            cv.destroyAllWindows()
        else:
            root = tk.Tk()
            root.withdraw()
            response = messagebox.askyesnocancel("Message", "Do you want to save the image?")
            
            if response == True:
                file_name = file_name.split('.')[0]
                cv.imwrite(f'{file_name}_resized.jpg', resized_img)
                messagebox.showinfo("Message", "Save success!")
            elif response == False:
                cv.destroyAllWindows()
            else:
                pass
            
    except:
        print("Something is wrong...")