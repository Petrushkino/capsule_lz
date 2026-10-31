import pandas as pd
import matplotlib.pyplot as plt

class GraphicStatistics:
    def __init__(self, data_source: str) -> None:
        self.data_source = data_source
        self.df = None

    def load_dataframe(self) -> None:
        self.df = pd.read_csv(self.data_source)
        
    def show_pie_chart(self) -> None:
        if self.df is None:
            self.load_dataframe()
            
        all_countries = self.df['country'].value_counts() #встречаемость стран в колонке и выстраиваемость их по убыванию
        
        top_10 = all_countries.head(10)
        
        others_count = all_countries.iloc[10:].sum()
        
        chart_data = pd.concat([top_10, pd.Series({'Другие (60 стран)': others_count})])
        
        plt.figure(figsize=(10, 8))
        
        plt.pie(chart_data, 
                labels=chart_data.index, 
                autopct='%1.1f%%', 
                startangle=140,
                pctdistance=0.85)
                
        center_circle = plt.Circle((0,0), 0.70, fc='white')
        plt.gca().add_artist(center_circle)
        
        plt.title('Количество игроков PS (Топ-10 стран)')
        plt.tight_layout()
        plt.show()