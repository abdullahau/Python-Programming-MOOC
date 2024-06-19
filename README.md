# Python Programming MOOC 2024

All my notes and solutions from the University of Helsinki's [Python Programming MOOC 2024](https://programming-24.mooc.fi/)

The exercises and examples are entirely implemented in Python 3. There are no requirements for external packages and/or libraries, except for Part 13 and 14, which requires Pygame.

Please feel free to message me for any questions or suggestions.

## References

Course Website: https://programming-24.mooc.fi/

## Files

```bash
|-- 0 - Master Notes.md
|-- 1 - Pygame.md
|-- 0 - Introduction to Programming Notes
|   |-- Data-Files
|   |-- Intro To Programming Exam - 04-05-2024
|   |   |-- Exam1.md
|   |   |-- Notes
|   |   |   |-- Exercise 1.py
|   |   |   |-- Exercise 2 copy.py
|   |   |   |-- Exercise 2.py
|   |   |   |-- Exercise 3.py
|   |   |   |-- statistics copy.txt
|   |   |   `-- statistics.txt
|   |   `-- Submissions
|   |       |-- ValueErrors.txt
|   |       |-- exercise1.py
|   |       |-- exercise2.py
|   |       |-- exercise3.py
|   |       `-- statistics.txt
|   |-- Part 1 - Arithmetic Operations.py
|   |-- Part 1 - Conditional Statements.py
|   |-- Part 1 - Prints & Inputs.py
|   |-- Part 2 - More Conditionals.py
|   |-- Part 2 - Simple Loops.py
|   |-- Part 3 - Debugging Example.py
|   |-- Part 3 - Defining Functions.py
|   |-- Part 3 - Loops with Conditions.py
|   |-- Part 3 - More Loops.py
|   |-- Part 3 - Strings.py
|   |-- Part 4 - Definite iteration.py
|   |-- Part 4 - Developing a larger programming project.py
|   |-- Part 4 - Grade Statistics - 2.py
|   |-- Part 4 - Grade Statistics.py
|   |-- Part 4 - Lists.py
|   |-- Part 4 - More Functions.py
|   |-- Part 4 - More strings and lists.py
|   |-- Part 4 - Print statement formatting.py
|   |-- Part 5 - Dictionary.py
|   |-- Part 5 - More Lists and Matrix.py
|   |-- Part 5 - References.py
|   |-- Part 5 - Student database.py
|   |-- Part 5 - Sudoku.py
|   |-- Part 5 - Test.ipynb
|   |-- Part 5 - Tuple.py
|   |-- Part 6 - Handling errors.py
|   |-- Part 6 - Reading Files.py
|   |-- Part 6 - Writing files.py
|   |-- Part 7 - Creating your own modules.py
|   |-- Part 7 - Data processing.py
|   |-- Part 7 - Modules.py
|   |-- Part 7 - More Python features.py
|   |-- Part 7 - Randomness.py
|   |-- Part 7 - Times and dates.py
|   `-- string_helper.py
|-- 1 - Advanced Course in Programming Notes
|   |-- Advanced Course in Programming Exam - 15-06-2024
|   |   |-- Exam.md
|   |   |-- Exercise 1.py
|   |   |-- Exercise 2.py
|   |   |-- Exercise 3-1.py
|   |   |-- Exercise 3.py
|   |   `-- recipes.txt
|   |-- Data-Files
|   |-- Part 10 - Access modifiers.py
|   |-- Part 10 - Class hierarchies.py
|   |-- Part 10 - Developing a larger application.py
|   |-- Part 10 - Object oriented programming techniques.py
|   |-- Part 11 - List comprehensions.py
|   |-- Part 11 - More comprehensions.py
|   |-- Part 11 - More recursion examples.py
|   |-- Part 11 - Recursion.py
|   |-- Part 12 - Functional programming.py
|   |-- Part 12 - Functions as arguments.py
|   |-- Part 12 - Generators.py
|   |-- Part 12 - Lambda Function Exercises.ipynb
|   |-- Part 12 - Regular expressions.py
|   |-- Part 13 - Animation.py
|   |-- Part 13 - Events.py
|   |-- Part 13 - More pygame techniques.py
|   |-- Part 13 - Pygame.py
|   |-- Part 14 - Finishing the game.py
|   |-- Part 14 - Game project.py
|   |-- Part 14 - Robot and boxes.py
|   |-- Part 8 - Classes and objects.py
|   |-- Part 8 - Defining classes.py
|   |-- Part 8 - Defining methods.py
|   |-- Part 8 - More examples of classes.py
|   |-- Part 8 - Objects and methods.py
|   |-- Part 9 - Class attributes.py
|   |-- Part 9 - Encapsulation.py
|   |-- Part 9 - More examples with classes.py
|   |-- Part 9 - Objects and references.py
|   |-- Part 9 - Objects as attributes.py
|   `-- Part 9 - Scope of methods.py
|-- Applications
|   |-- CoinPort
|   |   |-- coin.png
|   |   |-- door.png
|   |   |-- game.py
|   |   |-- monster.png
|   |   `-- robot.png
|   |-- CourseRecords Application
|   |   `-- main.py
|   |-- Hockey Statistics Application
|   |   |-- all.json
|   |   |-- hockey_statistics-v2.py
|   |   |-- hockey_statistics.py
|   |   `-- partial.json
|   |-- Maze Generator
|   |   |-- Maze generation copy.py
|   |   |-- Maze generation.py
|   |   `-- maze.txt
|   |-- OrderBook Application
|   |   |-- input.txt
|   |   |-- input2.txt
|   |   |-- input3.txt
|   |   |-- main.py
|   |   `-- test.py
|   |-- Pacman
|   |-- Part 9 - Objects as attributes - Example
|   |   |-- MainFunction.py
|   |   |-- completedcourse.py
|   |   |-- course.py
|   |   `-- student.py
|   |-- PhoneBook Application
|   |   |-- main.py
|   |   |-- main_expansion_v2.py
|   |   `-- phonebook.txt
|   |-- Rich The Robot
|   |   |-- coin.png
|   |   |-- door.png
|   |   |-- game.py
|   |   |-- monster.png
|   |   `-- robot.png
|   |-- Your-own-game
|   |   |-- coin.png
|   |   |-- door.png
|   |   |-- game.py
|   |   |-- monster.png
|   |   `-- robot.png
|   `-- sokoban
|       |-- README.md
|       |-- sokoban-english.py
|-- Data-Files
|-- Images
|-- README.md
|-- Reference Notes
|   |-- Algorithms.py
|   |-- Angles in Pygame.py
|   |-- Comprehensions.py
|   |-- Primes
|   |   |-- 10m_prime_sive.txt
|   |   |-- 1m_prime_sive_v0.txt
|   |   |-- Prime_Sieve_1.py
|   |   |-- Prime_Sieve_2.py
|   |   |-- Prime_Sieve_3.py
|   |   |-- Prime_Sieve_4.py
|   |   |-- Prime_Sieve_4a.py
|   |   |-- Prime_Sieve_5py
|   |   |-- Trial_Div_1.py
|   |   |-- Trial_Div_2.py
|   |   `-- solution_3
|   |       |-- Dockerfile
|   |       |-- PrimePY.py
|   |       |-- README.md
|   |       `-- tests
|   |           |-- __init__.py
|   |           `-- test_sieve.py
|   `-- f-string.py
|-- Slides
|   |-- Slides 1.pdf
|   |-- Slides 10.pdf
|   |-- Slides 11.pdf
|   |-- Slides 12.pdf
|   |-- Slides 2.pdf
|   |-- Slides 3.pdf
|   |-- Slides 4.pdf
|   |-- Slides 5.pdf
|   |-- Slides 6.pdf
|   |-- Slides 7.pdf
|   `-- Slides 8.pdf
|-- course-submission-files
|   |-- hy-adv-course-in-prog-exam-15062024
|   |   |-- Exam15062024-Exercise1
|   |   |-- Exam15062024-Exercise2
|   |   `-- Exam15062024-Exercise3
|   |-- hy-intro-to-programming-exam-04052024
|   |   |-- Exam04052024-Exercise1
|   |   |-- Exam04052024-Exercise2
|   |   `-- Exam04052024-Exercise3
|   `-- mooc-programming-24
|       |-- part01-01_emoticon
|       |-- part01-02_seven_brothers
|       |-- part01-03_row_your_boat
|       |-- part01-04_minutes_in_a_year
|       |-- part01-05_print_code
|       |-- part01-06_name_twice
|       |-- part01-07_name_and_exclamation_marks
|       |-- part01-08_name_and_address
|       |-- part01-09_utterances
|       |-- part01-10_story
|       |-- part01-10b_extra_space
|       |-- part01-11_arithmetics
|       |-- part01-12_print_a_single_line
|       |-- part01-13_times_five
|       |-- part01-14_name_and_age
|       |-- part01-15_seconds_in_a_day
|       |-- part01-16_product
|       |-- part01-17_sum_and_product
|       |-- part01-18_sum_and_mean
|       |-- part01-19_food_expenditure
|       |-- part01-20_students_in_groups
|       |-- part01-21_orwell
|       |-- part01-22_absolute_value
|       |-- part01-23_soup_or_no_soup
|       |-- part01-24_order_of_magnitude
|       |-- part01-25_calculator
|       |-- part01-26_temperatures
|       |-- part01-27_daily_wages
|       |-- part01-28_loyalty_bonus
|       |-- part01-29_what_to_wear_tomorrow
|       |-- part01-30_quadratic_formula
|       |-- part02-01_fix_syntax
|       |-- part02-02_number_of_characters
|       |-- part02-03_typecasting
|       |-- part02-04_age_of_maturity
|       |-- part02-05_greater_or_equal
|       |-- part02-06_elder
|       |-- part02-07_alphabetically_last
|       |-- part02-08_age_check
|       |-- part02-09_nephews
|       |-- part02-10_grades_and_points
|       |-- part02-11_fizzbuzz
|       |-- part02-12_leap_year
|       |-- part02-13_alphabetically_in_the_middle
|       |-- part02-14_gift_tax_calculator
|       |-- part02-15_shall_we_continue
|       |-- part02-16_input_validation
|       |-- part02-17_countdown
|       |-- part02-18_repeat_password
|       |-- part02-19_pin_and_number_of_attempts
|       |-- part02-20_next_leap_year
|       |-- part02-21_story
|       |-- part02-22_working_with_numbers
|       |-- part03-01_print_numbers
|       |-- part03-02_countdown
|       |-- part03-03_numbers
|       |-- part03-04_powers_of_two
|       |-- part03-05_powers_of_base_n
|       |-- part03-06_consecutive_sum_v1
|       |-- part03-07_consecutive_sum_v2
|       |-- part03-08_string_multiplied
|       |-- part03-09_longer_string
|       |-- part03-10_end_to_beginning
|       |-- part03-11_second_and_second_to_last
|       |-- part03-12_line_of_hashes
|       |-- part03-13_rectangle_of_hashes
|       |-- part03-14_underlining
|       |-- part03-15_right_aligned
|       |-- part03-16_framed_word
|       |-- part03-17_substrings_part_1
|       |-- part03-18_substrings_part_2
|       |-- part03-19_does_it_contain_vowels
|       |-- part03-20_find_first_substring
|       |-- part03-21_find_all_substrings
|       |-- part03-22_second_occurrence
|       |-- part03-23_multiplication
|       |-- part03-24_first_letters_of_words
|       |-- part03-25_factorial
|       |-- part03-26_flip_the_pairs
|       |-- part03-27_taking_turns
|       |-- part03-28_seven_brothers
|       |-- part03-29_first_character
|       |-- part03-30_mean
|       |-- part03-31_print_many_times
|       |-- part03-32_square_of_hashes
|       |-- part03-33_chessboard
|       |-- part03-34_word_squared
|       |-- part04-01_hello_visual_studio_code
|       |-- part04-02_line
|       |-- part04-03_box_of_hashes
|       |-- part04-04_square_of_hashes
|       |-- part04-05_square
|       |-- part04-06_triangle
|       |-- part04-07_shape
|       |-- part04-08_spruce
|       |-- part04-09_greatest_number
|       |-- part04-10_same_characters
|       |-- part04-11_first_second_last
|       |-- part04-12_change_value_of_item
|       |-- part04-13_add_items_to_list
|       |-- part04-14_addition_and_removal
|       |-- part04-15_same_word_twice
|       |-- part04-16_list_twice
|       |-- part04-17_length_of_list
|       |-- part04-18_mean
|       |-- part04-19_range_of_list
|       |-- part04-20_star_studded
|       |-- part04-21_negative_to_positive
|       |-- part04-22_list_of_stars
|       |-- part04-23_anagrams
|       |-- part04-24_palindromes
|       |-- part04-25_sum_of_positives
|       |-- part04-26_even_numbers
|       |-- part04-27_sum_of_lists
|       |-- part04-28_distinct_numbers
|       |-- part04-29_length_of_longest
|       |-- part04-30_shortest_in_list
|       |-- part04-31_all_longest_in_list
|       |-- part04-32_integers_to_strings
|       |-- part04-33_everything_reversed
|       |-- part04-34_most_common_character
|       |-- part04-35_no_vowels_allowed
|       |-- part04-36_no_shouting_allowed
|       |-- part04-37_neighbours_in_list
|       |-- part04-38_grade_statistics
|       |-- part05-01_longest_string
|       |-- part05-02_number_of_elements
|       |-- part05-03_go
|       |-- part05-04_sudoku_row
|       |-- part05-05_sudoku_column
|       |-- part05-06_sudoku_block
|       |-- part05-07_sudoku_grid
|       |-- part05-08_items_multiplied_by_two
|       |-- part05-09_remove_smallest
|       |-- part05-10_sudoku_print_and_add
|       |-- part05-11_sudoku_add_to_copy
|       |-- part05-12_tic_tac_toe
|       |-- part05-13_transpose_matrix
|       |-- part05-14_times_ten
|       |-- part05-15_factorials
|       |-- part05-16_histogram
|       |-- part05-17_phone_book_v1
|       |-- part05-18_phone_book_v2
|       |-- part05-19_invert_dictionary
|       |-- part05-20_numbers_spelled_out
|       |-- part05-21_movie_database
|       |-- part05-22_find_movies
|       |-- part05-23_create_tuple
|       |-- part05-24_oldest_person
|       |-- part05-25_older_people
|       |-- part05-26_student_database
|       |-- part05-27_letter_square
|       |-- part06-01_largest_number
|       |-- part06-02_fruit_market
|       |-- part06-03_matrix
|       |-- part06-04_course_grading_part_1
|       |-- part06-05_course_grading_part_2
|       |-- part06-06_course_grading_part_3
|       |-- part06-07_spellchecker
|       |-- part06-08_recipe_search
|       |-- part06-09_city_bikes
|       |-- part06-10_inscription
|       |-- part06-11_diary
|       |-- part06-12_filtering_file_contents
|       |-- part06-13_store_personal_data
|       |-- part06-14_course_grading_part_4
|       |-- part06-15_word_search
|       |-- part06-16_dictionary_file
|       |-- part06-17_read_input
|       |-- part06-18_parameter_validation
|       |-- part06-19_incorrect_lottery_numbers
|       |-- part07-01_hypotenuse
|       |-- part07-02_special_characters
|       |-- part07-03_fractions
|       |-- part07-04_lottery_numbers
|       |-- part07-05_password_generator_part_1
|       |-- part07-06_password_generator_part_2
|       |-- part07-07_dice_roller
|       |-- part07-08_random_words
|       |-- part07-09_how_old
|       |-- part07-10_valid_pic
|       |-- part07-11_screen_time
|       |-- part07-12_json_files
|       |-- part07-13_course_statistics
|       |-- part07-14_who_cheated
|       |-- part07-15_who_cheated_2
|       |-- part07-16_spellchecker_2
|       |-- part07-17_string_helper
|       |-- part07-18_own_programming_language
|       |-- part08-01_smallest_average
|       |-- part08-02_row_sums
|       |-- part08-03_list_years
|       |-- part08-04_shopping_list
|       |-- part08-05_book
|       |-- part08-06_three_classes
|       |-- part08-07_pet
|       |-- part08-08_older_book
|       |-- part08-09_books_of_genre
|       |-- part08-10_decreasing_counter
|       |-- part08-11_first_and_last_name
|       |-- part08-12_number_stats
|       |-- part08-13_stopwatch
|       |-- part08-14_clock
|       |-- part08-15_lunchcard
|       |-- part08-16_series
|       |-- part09-01_fastest_car
|       |-- part09-02_passing_submissions
|       |-- part09-03_baby_centre
|       |-- part09-04_lunchcard_and_paymentterminal
|       |-- part09-05_comparing_properties
|       |-- part09-06_pets
|       |-- part09-07_box_of_presents
|       |-- part09-08_shortest_in_room
|       |-- part09-09_car
|       |-- part09-10_recording
|       |-- part09-11_weather_station
|       |-- part09-12_service_charge
|       |-- part09-13_postcodes
|       |-- part09-14_list_helper
|       |-- part09-15_item_suitcase_hold
|       |-- part10-01_laptop_computer
|       |-- part10-02_game_museum
|       |-- part10-03_areas
|       |-- part10-04_word_game
|       |-- part10-05_supergroup
|       |-- part10-06_secret_magic_potion
|       |-- part10-07_money
|       |-- part10-08_simple_date
|       |-- part10-09_iterable_shopping_list
|       |-- part10-10_phone_book_v1
|       |-- part10-11_phone_book_v2
|       |-- part10-12_course_records
|       |-- part11-01_square_roots
|       |-- part11-02_rows_of_stars
|       |-- part11-03_best_exam_result
|       |-- part11-04_lengths
|       |-- part11-05_remove_smaller_than
|       |-- part11-06_begin_with_vowel
|       |-- part11-07_lottery_numbers
|       |-- part11-08_filter_forbidden
|       |-- part11-09_products_in_shopping_list
|       |-- part11-10_cheaper_properties
|       |-- part11-11_lengths_of_strings
|       |-- part11-12_most_common_words
|       |-- part11-13_add_numbers_to_list
|       |-- part11-14_recursive_sum
|       |-- part11-15_balanced_brackets
|       |-- part11-16_greatest_node
|       |-- part11-17_bosses_and_subordinates
|       |-- part11-18_order_book
|       |-- part11-19_order_book_application
|       |-- part12-01_remaining_stock
|       |-- part12-02_seasons
|       |-- part12-03_ratings
|       |-- part12-04_climbing_route
|       |-- part12-05_climbing_areas
|       |-- part12-06_ballplayers
|       |-- part12-07_product_search
|       |-- part12-08_even_numbers
|       |-- part12-09_prime_numbers
|       |-- part12-10_random_words
|       |-- part12-11_attempted_courses
|       |-- part12-12_filtering_attempts
|       |-- part12-13_credits
|       |-- part12-14_regular_expressions
|       |-- part12-15_hockey_statistics
|       |-- part13-01_four_robots
|       |-- part13-02_robots_row
|       |-- part13-03_hundred_robots
|       |-- part13-04_random_robots
|       |-- part13-05_vertical_movement
|       |-- part13-06_round_the_perimeter
|       |-- part13-07_two_robots
|       |-- part13-08_robot_circle
|       |-- part13-09_bouncing_ball
|       |-- part13-10_robot_invasion
|       |-- part13-11_four_directions
|       |-- part13-12_four_walls
|       |-- part13-13_two_players
|       |-- part13-14_robot_and_mouse
|       |-- part13-15_robot_location
|       |-- part13-16_clock
|       |-- part13-17_asteroids
|       `-- part14-01_own_game
`-- rage-programming-24-course-data
```
