from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random
from django.core.exceptions import ObjectDoesNotExist

PRAISE_TEXTS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
]


def fix_marks(schoolkid):
    updated_count = Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(
        points=5
    )
    print(f"Исправлено оценок: {updated_count}")
    return updated_count


def remove_chastisements(schoolkid):
    deleted_count, _ = Chastisement.objects.filter(schoolkid=child).delete()
    print(f"Удалено замечаний: {deleted_count}")
    return deleted_count


def create_commendation(schoolkid, subject_name):
    lesson = (
        Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_name,
        )
        .order_by("-date")
        .first()
    )
    if lesson is None:
        print(f"Урок{subject_name} не найден для ученика {child.full_name}")
    Commendation.objects.filter(
        schoolkid=child, subject=lesson.subject, created=lesson.date
    ).exists()
    praise_text = random.choice(PRAISE_TEXTS)
    Commendation.objects.create(
        text=praise_text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
    )
    print("Похвала создана!")


if __name__ == "__main__":
    try:
        child = Schoolkid.objects.get(full_name__contains="Фролов Иван")
        print(f"Ученик: {child.full_name}")
        fix_marks(child)
        remove_chastisements(child)
        create_commendation(child, "Математика")
    except ObjectDoesNotExist:  # Ловим исключение, если ученик не найден
        print("Ученик с фамилией 'Фролов' не найден.")
