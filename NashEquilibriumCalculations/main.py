from openpyxl import Workbook
from openpyxl.styles import PatternFill
from enum import Enum


class NashEquilibrium(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4
    NONE = 5


def write_results_of_nash_equilibrium_in_excel(tuples_array, excel_name):
    # Define colors for each Enum value
    color_map = {
        NashEquilibrium.TOP_LEFT: "00FF00",  # Green
        NashEquilibrium.TOP_RIGHT: "FF0000",  # Red
        NashEquilibrium.BOTTOM_LEFT: "FFFF00",  # Yellow
        NashEquilibrium.BOTTOM_RIGHT: "808080",  # Gray
    }

    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active

    # Define the header for the Excel sheet
    ws.append(["give_a", "give_b", "receive_a", "receive_b", "amount_of_nash_equilibrium", "Nash_Equilibriums", "",
               "1+(y_1-1)x_1", "y_1x_1", "1+(y_2-1)x_2", "y_2x_2"])

    # Populate the Excel sheet with data and highlight True results
    for row_index, (a, b, c, d, e, result_array) in enumerate(tuples_array, start=2):  # Start from the second row
        ws.cell(row=row_index, column=1, value=a)
        ws.cell(row=row_index, column=2, value=c)
        ws.cell(row=row_index, column=3, value=b)
        ws.cell(row=row_index, column=4, value=d)
        ws.cell(row=row_index, column=5, value=e)
        ws.cell(row=row_index, column=6, value=', '.join([r.name for r in result_array]))

        # Apply color to the row based on each Enum in result_array
        for r in result_array:
            if r in color_map:
                highlight_fill = PatternFill(start_color=color_map[r], end_color=color_map[r], fill_type="solid")
                for col_index in range(1, 6):  # Columns 1 to 5
                    ws.cell(row=row_index, column=col_index).fill = highlight_fill

        ws.cell(row=row_index, column=8, value=1 + ((c - 1) * a))
        ws.cell(row=row_index, column=9, value=c * a)
        ws.cell(row=row_index, column=10, value=1 + ((d - 1) * b))
        ws.cell(row=row_index, column=11, value=d * b)

        # a = x_1 and c = y_1
        # b= x_2 and d = y_2

        if 1 + (c - 1) * a > c * a:
            highlight_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
            for col_index in range(8, 10):  # Columns 8 to 9
                ws.cell(row=row_index, column=col_index).fill = highlight_fill

        if 1 + (d - 1) * b > d * b:
            highlight_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
            for col_index in range(10, 12):  # Columns 10 to 11
                ws.cell(row=row_index, column=col_index).fill = highlight_fill

    # Save the workbook
    wb.save(excel_name)


def calculate_matrix(matrix, give_a, receive_a, give_b, receive_b):
    # matrix is something like

    # [[(a1,a2),(b1,b2)]
    #  [(c1,c2),(d1,d2)]]

    # with a,b,c,d as ints
    new_matrix = [[(0, 0), (0, 0)],
                  [(0, 0), (0, 0)]]
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix)):
            t1, t2 = matrix[row_index][col_index]
            score_for_a = t1 * (1 - give_a) + receive_a * (t1 * give_a + t2 * give_b)
            score_for_b = t2 * (1 - give_b) + receive_b * (t1 * give_a + t2 * give_b)

            new_matrix[row_index][col_index] = (score_for_a, score_for_b)

    return new_matrix


def top_left_value(matrix):
    return matrix[0][0]


def top_right_value(matrix):
    return matrix[0][1]


def bottom_left_value(matrix):
    return matrix[1][0]


def bottom_right_value(matrix):
    return matrix[1][1]


def nash_equilibrium_is_top_left(matrix):
    return top_left_value(matrix)[0] > bottom_left_value(matrix)[0] and \
        top_left_value(matrix)[1] > top_right_value(matrix)[1]


def nash_equilibrium_is_top_right(matrix):
    return top_right_value(matrix)[0] > bottom_right_value(matrix)[0] and \
        top_left_value(matrix)[1] < top_right_value(matrix)[1]


def nash_equilibrium_is_bottom_left(matrix):
    return top_left_value(matrix)[0] < bottom_left_value(matrix)[0] and \
        bottom_left_value(matrix)[1] > bottom_right_value(matrix)[1]


def nash_equilibrium_is_bottom_right(matrix):
    return top_right_value(matrix)[0] < bottom_right_value(matrix)[0] and \
        bottom_left_value(matrix)[1] < bottom_right_value(matrix)[1]


def test_for_nash_equilibrium(m, excel_name):
    calculated_matrixes = []
    give_and_receive_for_matrixes = []

    for give_a in range(0, 11):
        for give_b in range(0, 11):
            for receive_a in range(0, 11):
                for receive_b in range(0, 11):
                    if receive_a + receive_b != 10:
                        continue

                    if give_a + give_b == 0:
                        continue

                    new_m = calculate_matrix(m, give_a / 10, receive_a / 10, give_b / 10, receive_b / 10)
                    nash_equilibriums = []

                    if nash_equilibrium_is_top_left(new_m):
                        calculated_matrixes.append(new_m)
                        nash_equilibriums.append(NashEquilibrium.TOP_LEFT)
                    if nash_equilibrium_is_top_right(new_m):
                        calculated_matrixes.append(new_m)
                        nash_equilibriums.append(NashEquilibrium.TOP_RIGHT)
                    if nash_equilibrium_is_bottom_left(new_m):
                        calculated_matrixes.append(new_m)
                        nash_equilibriums.append(NashEquilibrium.BOTTOM_LEFT)
                    if nash_equilibrium_is_bottom_right(new_m):
                        calculated_matrixes.append(new_m)
                        nash_equilibriums.append(NashEquilibrium.BOTTOM_RIGHT)

                    give_and_receive_for_matrixes.append(
                        (give_a / 10, receive_a / 10, give_b / 10, receive_b / 10, len(nash_equilibriums),
                         nash_equilibriums)
                    )

    write_results_of_nash_equilibrium_in_excel(give_and_receive_for_matrixes, excel_name)


if __name__ == '__main__':
    prisioner_dilema = [[(1, 1), (-1, 2)],
                        [(2, -1), (0, 0)]]

    test_for_nash_equilibrium(prisioner_dilema, "results/nash_results_for_prisioner_dilema.xlsx")

    battle_of_the_sexes = [[(2, 1), (0, 0)],
                           [(0, 0), (1, 2)]]

    test_for_nash_equilibrium(battle_of_the_sexes, "results/nash_results_for_battle_of_the_sexes.xlsx")

    stag_hunt = [[(4, 4), (0, 3)],
                 [(3, 0), (2, 2)]]

    test_for_nash_equilibrium(stag_hunt, "results/nash_results_for_battle_of_the_sexes.xlsx")

    coordination_game = [[(3, 3), (0, 0)],
                         [(0, 0), (2, 2)]]

    test_for_nash_equilibrium(coordination_game, "results/nash_results_for_coordination_game.xlsx")

    matching_pennies = [[(1, -1), (-1, 1)],
                        [(-1, 1), (1, -1)]]

    test_for_nash_equilibrium(matching_pennies, "results/nash_results_for_matching_pennies.xlsx")

    # test_game = [[(1, 3), (2, 1)],
    #             [(2, 1), (-10, -10)]]

    # test_for_nash_equilibrium(test_game, "results/nash_results_for_test_game.xlsx")
