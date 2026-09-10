"""
Takes two inputs and modulos the first off the second
Carter Quarles - Spetember 2026
"""

def main() -> None:
  

  # input
  n: int = int(input())
  m: int = int(input())

  # processing
  leftover: int = n % m
  
  # output
  print(leftover)

if __name__ == "__main__":
  main()
    
