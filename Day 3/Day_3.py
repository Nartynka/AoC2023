import re

sum = 0

with open("input.txt", "r") as file:
   lines = file.readlines()
   for i in range(len(lines)):
      line = lines[i].strip()
      prev_line = lines[i-1].strip() if i > 0 else ""
      curr_line = lines[i].strip()
      next_line = lines[i+1].strip() if i < len(lines)-1 else ""

      numbers = re.finditer(r"\d+", curr_line)

      # Process one line
      for curr_num in numbers:
         # Porcess one number
         num_len = curr_num.end()-curr_num.start()

         is_valid = False

         before = after = "."
         abv_diag_l = abv_first = abv_sec = abv_third = abv_diag_r = "."
         btm_diag_l = btm_first = btm_sec = btm_third = btm_diag_r = "."

         ### CURRENT LINE
         # before
         if curr_num.start() > 0:
            before = curr_line[curr_num.start()-1]
         # after 
         if curr_num.end() < len(curr_line):
            after = curr_line[curr_num.end()]

         if before != "." or after != ".":
            is_valid = True


         ### LINE ABOVE
         if prev_line != "" and not is_valid:
            # diagonal above left
            if curr_num.start() > 0:
               abv_diag_l = prev_line[curr_num.start()-1]
            # above first number
            if curr_num.start() >= 0:
               abv_first = prev_line[curr_num.start()]
            # above second number
            if(num_len > 1):
               abv_sec = prev_line[curr_num.start()+1]
            # above third number
            if(num_len > 2):
               abv_third = prev_line[curr_num.start()+2]
            # diagonal above right
            if curr_num.end() < len(prev_line):
               abv_diag_r = prev_line[curr_num.end()]

            if abv_diag_l != "." or abv_first != "." or abv_sec != "." or abv_third != "." or abv_diag_r != ".":
               is_valid = True

         ### LINE UNDER
         if next_line != "" and not is_valid:
            # diagonal under left
            if curr_num.start() > 0:
               btm_diag_l = next_line[curr_num.start()-1]
            # under first number
            if curr_num.start() >= 0:
               btm_first = next_line[curr_num.start()]
            # under second number
            if(num_len > 1):
               btm_sec = next_line[curr_num.start()+1]
            # under third number
            if(num_len > 2):
               btm_third = next_line[curr_num.start()+2]
            # diagonal under right
            if curr_num.end() < len(next_line):
               btm_diag_r = next_line[curr_num.end()]

            if btm_diag_l != "." or btm_first != "." or btm_sec != "." or btm_third != "." or btm_diag_r != ".":
               is_valid = True

         if is_valid:
            sum += int(curr_num.group())
      print(sum, "\n")
