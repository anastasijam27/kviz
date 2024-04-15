1) Klonirate repozitorijum
2) Ako radite front, otvorite terminal:
   cd .\frontend\
   npm install
   npm run dev -- --host (za runovanje aplikacije)
3) Ako radite back, otvorite terminal:
   cd backend
   Set-ExecutionPolicy Unrestricted -Scope Process
   python -m virtualenv env
   .\env\Scripts\activate
   pip install -r requirements.txt
