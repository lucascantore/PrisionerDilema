# players
from players.teammates_lucifer.TeammateLuciferPointGiver import TeammateLuciferPointGiver
from players.teammates_lucifer.TeammateLuciferPointReceiver import TeammateLuciferPointReceiver
from players.Lucifer import Lucifer
from players.Random import Random
from players.GoodBoy import GoodBoy
from players.TipForTat import TipForTat
from players.teammates_tipfortat.TeammateTipForTatPointGiver import TeammateTipForTatPointGiver
from players.teammates_tipfortat.TeammateTipForTatPointReceiver import TeammateTipForTatPointReceiver

from Prisoner import create_dynamic_prisoner_class

# tournament
from Tournament import run_round_robin_tournament

# excel formatting
import pandas as pd
from openpyxl import load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import PatternFill
import openpyxl
import math
from itertools import product


def list_of_players(base_player, amount_of_players):
    player_list = []
    for i in range(amount_of_players):
        player_list = player_list + [create_dynamic_prisoner_class(base_player, f"{base_player.name()}_{i}")]

    return player_list


# we only support up to 675 players
def excel_column_number_for(number):
    first_letter_index = math.floor(number / 26)
    second_letter_index = number % 26

    if first_letter_index > 0:
        return f"{chr(65 + first_letter_index)}{chr(65 + second_letter_index)}"
    else:
        return f"{chr(65 + second_letter_index)}"


def format_results_to_excel(results, competing_players, excel_name):
    data = {
        "Games Played": list(results.keys())
    }

    for element in competing_players:
        data[element.name()] = []

    for key in results:
        for element in results[key]:
            data[element["name"]] = data[element["name"]] + [element["score"]]

    df = pd.DataFrame(data)
    df.to_excel(excel_name, index=False)

    wb = load_workbook(excel_name)
    ws = wb.active

    highlight_fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')

    for row in range(2, len(results.keys()) + 2):
        formula = f'B{row}=MAX($B{row}:${excel_column_number_for(len(competing_players))}{row})'
        rule = FormulaRule(formula=[formula], fill=highlight_fill)

        # Apply the rule to the row
        ws.conditional_formatting.add(f'B{row}:{excel_column_number_for(len(competing_players))}{row}', rule)

    wb.save(excel_name)  # Save to a new file or overwrite the existing one


def run_experiment_with(competing_agents, max_n_rounds, excel_name):
    print("started experiment for: ", list(map(lambda a: a.name(), competing_agents)))
    results = {}
    n_rounds = 5
    while n_rounds <= max_n_rounds:
        results[f"{n_rounds}"] = run_round_robin_tournament(competing_agents, n_rounds)
        if n_rounds < 100:
            n_rounds += 5
        else:
            n_rounds += 10

    format_results_to_excel(results, competing_agents, excel_name)


def teammates_lucifer_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(Lucifer, 1),
        max_rounds,
        "experiment_results/1_teammates_lucifer_vs_lucifer.xlsx"
    )


def teammates_lucifer_vs_random_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(Lucifer, 1)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/2_teammates_lucifer_vs_random_vs_lucifer.xlsx"
    )


def teammates_lucifer_vs_goodboy_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(Lucifer, 1)
        + list_of_players(GoodBoy, 5),
        max_rounds,
        "experiment_results/3_teammates_lucifer_vs_goodboy_vs_lucifer.xlsx"
    )


def teammates_lucifer_vs_goodboy_vs_random_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(Lucifer, 5)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/4_teammates_lucifer_vs_goodboy_vs_random_vs_lucifer.xlsx"
    )


def teammates_lucifer_vs_goodboy_vs_random_vs_single_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(TipForTat, 1)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/5_teammates_lucifer_vs_goodboy_vs_random_vs_single_tipfortat.xlsx"
    )


def teammates_lucifer_vs_goodboy_vs_random_vs_ten_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(TipForTat, 10)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/6_teammates_lucifer_vs_goodboy_vs_random_vs_ten_tipfortat.xlsx"
    )


def teammates_lucifer_vs_goodboy_vs_random_vs_fifteen_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(TipForTat, 15)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/7_teammates_lucifer_vs_goodboy_vs_random_vs_fifteen_tipfortat.xlsx"
    )


def teammates_lucifer_vs_three_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(TipForTat, 3),
        max_rounds,
        "experiment_results/8_teammates_lucifer_vs_three_tipfortat.xlsx"
    )


def teammates_tipfortat_vs_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(TipForTat, 5),
        max_rounds,
        "experiment_results/9_teammates_tipfortat_vs_tipfortat.xlsx"
    )


def teammates_tipfortat_vs_random_vs_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(TipForTat, 5)
        + list_of_players(Random, 5),
        max_rounds,
        "experiment_results/10_teammates_tipfortat_vs_random_vs_tipfortat.xlsx"
    )


def teammates_tipfortat_vs_random_vs_goodboy_vs_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(TipForTat, 5)
        + list_of_players(Random, 5)
        + list_of_players(GoodBoy, 5),
        max_rounds,
        "experiment_results/11_teammates_tipfortat_vs_random_vs_goodboy_vs_tipfortat.xlsx"
    )


def teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer_vs_tipfortat(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(TipForTat, 5)
        + list_of_players(Random, 5)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Lucifer, 3),
        max_rounds,
        "experiment_results/12_teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer_vs_tipfortat.xlsx"
    )


def teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(Random, 5)
        + list_of_players(GoodBoy, 5)
        + list_of_players(Lucifer, 1),
        max_rounds,
        "experiment_results/13_teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer.xlsx"
    )


def teammates_tipfortat_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(Lucifer, 1),
        max_rounds,
        "experiment_results/14_teammates_tipfortat_vs_lucifer.xlsx"
    )


def teammates_tipfortat_vs_random_vs_lucifer(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver]
        + list_of_players(Random, 5)
        + list_of_players(Lucifer, 1),
        max_rounds,
        "experiment_results/15_teammates_tipfortat_vs_random_vs_lucifer.xlsx"
    )


def teammates_tipfortat_vs_teammates_lucifer_vs_random_vs_tipfortat_vs_lucifer_vs_goodboy(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
        + list_of_players(Random, 5)
        + list_of_players(TipForTat, 5)
        + list_of_players(Lucifer, 5)
        + list_of_players(GoodBoy, 5),
        max_rounds,
        "experiment_results/16_teammates_tipfortat_vs_teammates_lucifer_vs_random_vs_tipfortat_vs_lucifer_vs_goodboy.xlsx"
    )


def multiple_everything_with_all_agents(max_rounds):
    range_of_players = range(1, 6)
    result_number = 17
    for num_random_players, num_tipfortat_players, num_lucifer_players, num_goodboy_players in product(range_of_players,
                                                                                                       repeat=4):
        run_experiment_with(
            [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
             TeammateLuciferPointGiver, TeammateLuciferPointReceiver]
            + list_of_players(Random, num_random_players)
            + list_of_players(TipForTat, num_tipfortat_players)
            + list_of_players(Lucifer, num_lucifer_players)
            + list_of_players(GoodBoy, num_goodboy_players),
            max_rounds,
            f"experiment_results/{result_number}_teammates_tipfortat_vs_teammates_lucifer_vs_{num_random_players}random_vs_{num_tipfortat_players}tipfortat_vs_{num_lucifer_players}lucifer_vs_{num_goodboy_players}goodboy.xlsx"
        )
        result_number = result_number + 1


def analyze_final_results():
    range_of_players = range(1, 6)
    result_number = 17

    # Create a new workbook to store the results
    result_wb = openpyxl.Workbook()
    result_sheet = result_wb.active
    result_sheet.title = "Analysis Results"

    # Write headers to the result sheet
    result_sheet.cell(row=1, column=1, value="File Name")
    result_sheet.cell(row=1, column=2, value="Value from Row 1")

    # Variable to keep track of the row in the result sheet
    result_row = 2

    for num_random_players, num_tipfortat_players, num_lucifer_players, num_goodboy_players in product(range_of_players,
                                                                                                       repeat=4):
        filepath = f"experiment_results/{result_number}_teammates_tipfortat_vs_teammates_lucifer_vs_{num_random_players}random_vs_{num_tipfortat_players}tipfortat_vs_{num_lucifer_players}lucifer_vs_{num_goodboy_players}goodboy.xlsx"

        # Load the workbook and select the active sheet
        wb = openpyxl.load_workbook(filepath)
        sheet = wb.active

        # Find the number of columns between 9 and 21 (in row 50)
        row_50_values = []
        for col in range(2, 22):  # Check up to column 21 (assuming max 21 columns)
            cell_value = sheet.cell(row=50, column=col).value
            if cell_value is not None:  # If there's a value in the cell, consider it
                row_50_values.append(cell_value)

        # Get the column with the highest value in row 50
        max_value = max(row_50_values)
        max_column_index = row_50_values.index(max_value) + 2  # Column index starts from 1

        # Get the value from row 1 in the same column
        value_in_row_1 = sheet.cell(row=1, column=max_column_index).value

        # Write the result to the new Excel sheet
        result_sheet.cell(row=result_row, column=1, value=filepath)  # File name
        result_sheet.cell(row=result_row, column=2, value=value_in_row_1)  # Value from row 1

        # Move to the next row in the result sheet
        result_row += 1

        result_number = result_number + 1

    result_wb.save("experiment_results/analysis_results.xlsx")





def run_all_experiments():
    max_rounds = 2500
    # teammates_lucifer_vs_lucifer(max_rounds)
    # teammates_lucifer_vs_random_vs_lucifer(max_rounds)
    # teammates_lucifer_vs_goodboy_vs_lucifer(max_rounds)
    # teammates_lucifer_vs_goodboy_vs_random_vs_lucifer(max_rounds)
    # teammates_lucifer_vs_goodboy_vs_random_vs_single_tipfortat(max_rounds)
    # teammates_lucifer_vs_goodboy_vs_random_vs_ten_tipfortat(max_rounds)
    # teammates_lucifer_vs_goodboy_vs_random_vs_fifteen_tipfortat(max_rounds)
    # teammates_lucifer_vs_three_tipfortat(max_rounds)
    # teammates_tipfortat_vs_tipfortat(max_rounds)
    # teammates_tipfortat_vs_random_vs_tipfortat(max_rounds)
    # teammates_tipfortat_vs_random_vs_goodboy_vs_tipfortat(max_rounds)
    # teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer_vs_tipfortat(max_rounds)
    # teammates_tipfortat_vs_random_vs_goodboy_vs_lucifer(max_rounds)
    # teammates_tipfortat_vs_lucifer(max_rounds)
    # teammates_tipfortat_vs_random_vs_lucifer(max_rounds)
    # teammates_tipfortat_vs_teammates_lucifer_vs_random_vs_tipfortat_vs_lucifer_vs_goodboy(max_rounds)
    # multiple_everything_with_all_agents(max_rounds)
    analyze_final_results()

