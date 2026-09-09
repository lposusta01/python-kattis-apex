"""
Add numbers and print total
Elizabeth Posusta - Sep 2026
"""

def main() -> None:
  # input

  hannes: int = int(input("How many cars did Hannes park?"))
  arnar: int = int(input("How many cars did Arnar park?"))
  # processing

  total: int = hannes + arnar
  
  # output

  print(total)


if __name__ == "__main__":
  main()
    
