from graph_stats import GraphicStatistics
from logger import log_decorator

@log_decorator
def run_graphics_task(file_path: str) -> None:
    print(f"Обработка файла: {file_path}")
    stats = GraphicStatistics(file_path)
    
    try:
        stats.show_pie_chart()
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except KeyError as e:
        print(f"Ошибка: В датасете не найдена колонка {e}.")

def main() -> None:    
    dataset_name = "playstation_players.csv"
    run_graphics_task(dataset_name)
    

if __name__ == "__main__":
    main()