from fastapi import APIRouter,status,HTTPException
from validations.question import Question
from main import db_dependency
from models.model import Questions,Choices

router = APIRouter()

@router.get("/")
def root():
    return {"message" : "Hello World"}

@router.get("/questions",status_code=status.HTTP_200_OK)
async def read_all_questions(db: db_dependency):
    result = db.query(Questions).all()
    return result

@router.get("/questions/{question_id}",status_code=status.HTTP_200_OK)
async def read_question(question_id: int,db : db_dependency):
    result = db.query(Questions).filter(Questions.id==question_id).first()
    if not result:
        raise HTTPException(status_code=404,detail="result not found")
    return result


@router.post("/questions",status_code=status.HTTP_201_CREATED)
async def create_question(question : Question,db:db_dependency):
    db_question = Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh()
    
    for choice in question.choices:
        db_choice = Choices(choice_text=choice.choice_text,is_correct=choice.is_correct,question_id=db_question.id)
        db.add(db_choice)
    db.commit()
    db.refresh()
    
@router.get("/choices/{question_id}",status_code=status.HTTP_200_OK)
async def read_choices(question_id : int, db:db_dependency):
    result = db.query(Choices).filter(Choices.question_id==question_id).all()
    if not result:
        raise HTTPException(status_code=404,detail="Choices not found")
    return result