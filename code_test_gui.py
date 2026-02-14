import tkinter as tk
from tkinter import ttk


# Reuse the original functions
def split_string_by_spaces(input_string):
    return input_string.split()


def count_words(input_string):
    words = input_string.split()
    return len(words)


class StringAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("String Analyzer")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Define modern colors
        bg_color = "#f0f2f5"
        accent_color = "#0084ff"
        text_color = "#1c1e21"
        
        style.configure("TFrame", background=bg_color)
        style.configure("TLabel", background=bg_color, foreground=text_color)
        style.configure("TLabelframe", background=bg_color, foreground=text_color)
        style.configure("TLabelframe.Label", background=bg_color, foreground=text_color)
        style.configure("TButton", font=("Segoe UI", 10))
        style.map("TButton", 
                 background=[("active", accent_color)],
                 foreground=[("active", "white")])
        
        self.root.configure(bg=bg_color)
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Main frame
        main_frame = ttk.Frame(root, padding="24")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="String Analyzer Tool", 
                               font=("Segoe UI", 18, "bold"), foreground=accent_color)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 16), sticky=tk.W)
        
        # Input label
        input_label = ttk.Label(main_frame, text="Enter a string:", 
                               font=("Segoe UI", 11, "bold"))
        input_label.grid(row=1, column=0, sticky=tk.W, pady=(8, 4))
        
        # Input text widget with border
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=2, column=0, columnspan=2, pady=(0, 16), 
                        sticky=(tk.W, tk.E, tk.N, tk.S))
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(0, weight=1)
        
        scrollbar = ttk.Scrollbar(input_frame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.input_text = tk.Text(input_frame, height=6, width=60, 
                                  font=("Segoe UI", 10), wrap=tk.WORD,
                                  bg="white", fg=text_color, relief=tk.FLAT,
                                  borderwidth=1, yscrollcommand=scrollbar.set)
        self.input_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.input_text.yview)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=12)
        
        # Process button
        process_button = ttk.Button(button_frame, text="Analyze", 
                                   command=self.analyze_string, width=15)
        process_button.pack(side=tk.LEFT, padx=6)
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear", 
                                 command=self.clear_all, width=15)
        clear_button.pack(side=tk.LEFT, padx=6)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Results", 
                                      padding="16", relief=tk.FLAT)
        results_frame.grid(row=4, column=0, columnspan=2, pady=(0, 16), 
                          sticky=(tk.W, tk.E, tk.N, tk.S))
        results_frame.columnconfigure(1, weight=1)
        results_frame.rowconfigure(2, weight=1)
        
        # Word count label
        word_count_label = ttk.Label(results_frame, text="Word Count:", 
                                    font=("Segoe UI", 11, "bold"))
        word_count_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 12))
        
        self.word_count_result = ttk.Label(results_frame, text="0", 
                                          font=("Segoe UI", 20, "bold"), 
                                          foreground=accent_color)
        self.word_count_result.grid(row=0, column=1, sticky=tk.W, padx=20)
        
        # Split result label
        split_label = ttk.Label(results_frame, text="Split Words:", 
                               font=("Segoe UI", 11, "bold"))
        split_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(12, 6))
        
        # Split result text widget with scrollbar
        split_frame = ttk.Frame(results_frame)
        split_frame.grid(row=2, column=0, columnspan=2, pady=(0, 0), 
                        sticky=(tk.W, tk.E, tk.N, tk.S))
        split_frame.columnconfigure(0, weight=1)
        split_frame.rowconfigure(0, weight=1)
        
        split_scrollbar = ttk.Scrollbar(split_frame)
        split_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.split_result = tk.Text(split_frame, height=6, width=50, 
                                    font=("Segoe UI", 10), wrap=tk.WORD, 
                                    state=tk.DISABLED, bg="white", 
                                    fg=text_color, relief=tk.FLAT, 
                                    borderwidth=1, yscrollcommand=split_scrollbar.set)
        self.split_result.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        split_scrollbar.config(command=self.split_result.yview)
    
    def analyze_string(self):
        input_string = self.input_text.get("1.0", tk.END).strip()
        
        if not input_string:
            self.word_count_result.config(text="0")
            self.split_result.config(state=tk.NORMAL)
            self.split_result.delete("1.0", tk.END)
            self.split_result.config(state=tk.DISABLED)
            return
        
        # Get results
        split_words = split_string_by_spaces(input_string)
        word_count = count_words(input_string)
        
        # Update word count
        self.word_count_result.config(text=str(word_count))
        
        # Update split result
        self.split_result.config(state=tk.NORMAL)
        self.split_result.delete("1.0", tk.END)
        self.split_result.insert("1.0", "\n".join(split_words))
        self.split_result.config(state=tk.DISABLED)
    
    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.word_count_result.config(text="0")
        self.split_result.config(state=tk.NORMAL)
        self.split_result.delete("1.0", tk.END)
        self.split_result.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = StringAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
