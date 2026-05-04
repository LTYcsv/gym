"""
Seed: exercise library + V-Shape program.
Run: python -m app.seed
"""
from app.database import SessionLocal, engine
from app.models import Base, Exercise, Program, WorkoutDay, WorkoutExercise

Base.metadata.create_all(bind=engine)

EXERCISES = [
    # ── BACK ──
    dict(name="Подтягивания широким хватом", muscle_group="back",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Хват шире плеч, лопатки сведены вниз перед началом. Тяни грудь к перекладине, локти уводи вниз и назад. В нижней точке — полное выпрямление рук."),
    dict(name="Тяга штанги в наклоне", muscle_group="back",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Наклон 45°, спина прямая. Тяни штангу к поясу, локти вдоль тела. В верхней точке — пауза и сжатие лопаток."),
    dict(name="Тяга верхнего блока широким хватом", muscle_group="back",
         types=["hypertrophy"], equipment=["cable"],
         technique="Широкий хват, тяни к верхней части груди. Лопатки сводятся в нижней точке."),
    dict(name="Тяга горизонтального блока", muscle_group="back",
         types=["hypertrophy"], equipment=["cable"],
         technique="Узкий хват, тяни к животу. Лопатки сводятся — держи спину прямой."),
    dict(name="Тяга гантели одной рукой", muscle_group="back",
         types=["strength", "hypertrophy"], equipment=["dumbbells"],
         technique="Колено и рука на скамье. Тяни к поясу, локоть уходит высоко вверх. Не скручивай корпус."),
    dict(name="Подтягивания нейтральным хватом", muscle_group="back",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Ладони смотрят друг на друга. Чуть проще широкого хвата — хорошо для новичков."),
    dict(name="Тяга верхнего блока за голову", muscle_group="back",
         types=["hypertrophy"], equipment=["cable"],
         technique="Широкий хват, голову наклони вперёд. Тяни к задней части шеи."),
    # ── CHEST ──
    dict(name="Жим штанги на наклонной скамье", muscle_group="chest",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Угол скамьи 30–45°. Хват чуть шире плеч, лопатки сведены и прижаты. Опускай медленно (2 сек). Жми взрывно вверх."),
    dict(name="Жим штанги лёжа", muscle_group="chest",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват чуть шире плеч. Лопатки сведены и прижаты к скамье. Опускай к нижней части груди. Жми взрывно."),
    dict(name="Жим гантелей лёжа", muscle_group="chest",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Гантели по бокам груди, локти 45–75° к корпусу. Жми и своди гантели в верхней точке."),
    dict(name="Жим гантелей на наклонной", muscle_group="chest",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Угол 30–45°. Гантели по бокам груди, локти чуть ниже линии плеч. Своди гантели вверху."),
    dict(name="Кроссовер в кабельной раме", muscle_group="chest",
         types=["hypertrophy"], equipment=["cable"],
         technique="Блоки сверху. Небольшой наклон вперёд. Своди руки дугой, слегка скрещивая в нижней точке."),
    dict(name="Разведение гантелей лёжа", muscle_group="chest",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Лёжа на скамье, гантели над грудью. Опускай в стороны с лёгким сгибом в локтях до ощущения растяжки."),
    dict(name="Отжимания на брусьях", muscle_group="chest",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Наклонись вперёд при отжимании — акцент на грудь. Опускайся медленно."),
    dict(name="Пуловер с гантелью", muscle_group="chest",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Лёжа поперёк скамьи. Опускай гантель за голову на прямых руках — ощущение растяжки в груди."),
    # ── SHOULDERS ──
    dict(name="Жим гантелей сидя", muscle_group="shoulders",
         types=["strength", "hypertrophy"], equipment=["dumbbells"],
         technique="Спина прямая, гантели на уровне ушей. Жми строго вверх. В верхней точке руки почти прямые."),
    dict(name="Разведение гантелей в стороны", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Лёгкий наклон вперёд, локоть чуть согнут. Подними до уровня плеча — не выше. Медленное опускание 3 сек."),
    dict(name="Тяга к подбородку", muscle_group="shoulders",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Узкий хват. Тяни к подбородку — локти ведут движение выше кистей."),
    dict(name="Жим штанги стоя (армейский)", muscle_group="shoulders",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват чуть шире плеч. Жми строго вверх над головой. Не прогибай поясницу."),
    dict(name="Жим Арнольда", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Начало — ладони к себе, гантели у подбородка. В процессе жима разворачивай ладони наружу."),
    dict(name="Разведение в наклоне (задняя дельта)", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Наклон 45–80°. Руки слегка согнуты. Разводи строго назад и вверх — не в стороны."),
    dict(name="Подъём гантелей перед собой", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Руки слегка согнуты. Поднимай до уровня плеч — не выше. Медленный негатив."),
    # ── TRICEPS ──
    dict(name="Трицепсовый блок (верёвка)", muscle_group="triceps",
         types=["hypertrophy"], equipment=["cable"],
         technique="Блок на верхнем уровне. Локти плотно прижаты к корпусу. Разгибай вниз и немного врозь."),
    dict(name="Французский жим лёжа", muscle_group="triceps",
         types=["strength", "hypertrophy"], equipment=["barbell", "dumbbells"],
         technique="EZ-гриф или гантели. Локти неподвижны, смотрят в потолок. Опускай к верхней части лба — медленно."),
    dict(name="Жим узким хватом лёжа", muscle_group="triceps",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват 20–25 см. Локти строго вдоль тела. Жми и полностью выпрямляй руки."),
    dict(name="Разгибание гантели из-за головы", muscle_group="triceps",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Одной или двумя руками. Локти фиксированы у головы. Медленно."),
    # ── BICEPS ──
    dict(name="Сгибание рук со штангой", muscle_group="biceps",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват на ширине плеч. Локти неподвижны у корпуса. Пауза 1 сек в верхней точке. Медленно опускай (2–3 сек)."),
    dict(name="Молотковые сгибания гантелями", muscle_group="biceps",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Нейтральный хват (ладони внутрь). Локти фиксированы — поочерёдно или вместе."),
    dict(name="Сгибания на скамье Скотта", muscle_group="biceps",
         types=["hypertrophy"], equipment=["barbell", "dumbbells"],
         technique="Руки полностью фиксированы на подушке. Полное разгибание в нижней точке."),
    dict(name="Концентрированные сгибания", muscle_group="biceps",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Локоть упирается во внутреннюю поверхность бедра. Максимальное сокращение — пауза 2 сек."),
    # ── QUADRICEPS ──
    dict(name="Приседания со штангой", muscle_group="quadriceps",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Штанга на трапециях. Стопы чуть шире плеч, носки 15–30°. Присед — бёдра ниже параллели. Вставай через пятки."),
    dict(name="Жим ногами (платформа)", muscle_group="quadriceps",
         types=["hypertrophy"], equipment=["machine"],
         technique="Широкая постановка ног — середина и верх платформы. Не блокируй колени. Опускай до угла 90°."),
    dict(name="Фронтальные приседания", muscle_group="quadriceps",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Штанга на передних дельтах, руки скрещены или вытянуты. Колени вперёд. Спина прямая."),
    dict(name="Разгибания ног в тренажёре", muscle_group="quadriceps",
         types=["hypertrophy"], equipment=["machine"],
         technique="Сидя. Разгибай до полного выпрямления. Пауза 1 сек. Медленный негатив (3 сек)."),
    dict(name="Выпады со штангой", muscle_group="quadriceps",
         types=["strength", "hypertrophy"], equipment=["barbell", "dumbbells"],
         technique="Шаг вперёд — заднее колено почти касается пола. Не заваливай переднее колено внутрь."),
    dict(name="Болгарские сплит-приседания", muscle_group="quadriceps",
         types=["hypertrophy", "strength"], equipment=["dumbbells", "barbell"],
         technique="Задняя нога на скамье. Присед на одной ноге — колено не выходит за носок."),
    # ── HAMSTRINGS ──
    dict(name="Румынская тяга", muscle_group="hamstrings",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Штанга у бёдер, лёгкий сгиб в коленях. Наклоняйся вперёд, отводя таз назад. До ощущения растяжки бицепса бедра."),
    dict(name="Сгибание ног лёжа", muscle_group="hamstrings",
         types=["hypertrophy"], equipment=["machine"],
         technique="Ось тренажёра — на уровне колена. Сгибай до угла 90° и немного дальше. Медленное разгибание (3 сек)."),
    # ── LOWER BACK ──
    dict(name="Гиперэкстензия", muscle_group="lower_back",
         types=["strength", "hypertrophy"], equipment=["machine", "bodyweight"],
         technique="Таз на подушке тренажёра. Опустись до параллели с полом. Поднимай корпус до прямой линии — не переразгибай поясницу."),
    # ── CORE ──
    dict(name="Скручивания с весом", muscle_group="core",
         types=["strength", "hypertrophy"], equipment=["bodyweight"],
         technique="Блин на груди или за головой. Скручивай — не поднимай всё тело. Поясница прижата к полу."),
    dict(name="Подъём ног в висе", muscle_group="core",
         types=["strength", "calisthenics"], equipment=["bodyweight"],
         technique="Висишь на перекладине. Поднимай прямые или согнутые ноги до параллели — или выше."),
    dict(name="Планка", muscle_group="core",
         types=["strength", "hypertrophy", "calisthenics", "cardio", "hiit"], equipment=["bodyweight"],
         technique="Тело — прямая линия от головы до пят. Не поднимай таз вверх и не проваливай поясницу."),
    # ── CARDIO / HIIT specific ──
    dict(name="Берпи", muscle_group="core",
         types=["cardio", "hiit"], equipment=["bodyweight"],
         technique="Из стойки — присед, упор лёжа, отжимание (опционально), снова упор, прыжок вверх с хлопком над головой."),
    dict(name="Прыжки на скакалке", muscle_group="calves",
         types=["cardio", "hiit"], equipment=["bands"],
         technique="Прыгай на носках, запястья делают вращение. Начни с 30 сек, наращивай постепенно."),
    dict(name="Горные альпинисты", muscle_group="core",
         types=["cardio", "hiit"], equipment=["bodyweight"],
         technique="Упор лёжа. Поочерёдно подтягивай колени к груди в быстром темпе. Корпус неподвижен."),
    # ── CALVES ──
    dict(name="Подъём на носки стоя", muscle_group="calves",
         types=["hypertrophy", "strength"], equipment=["machine", "bodyweight"],
         technique="Медленный подъём, полный диапазон — пятка максимально вниз, носок вверх. Пауза вверху 2 сек."),
]

# V-Shape program days & exercises
VSHAPE_DAYS = [
    {
        "label": "День A", "title": "Спина + Плечи", "subtitle": "Ширина · Тяга · Дельты",
        "exercises": [
            ("Подтягивания широким хватом",     4, "6–10", 90),
            ("Тяга штанги в наклоне",           4, "8–10", 90),
            ("Жим гантелей сидя",               4, "10–12", 75),
            ("Разведение гантелей в стороны",   3, "12–15", 60),
            ("Тяга к подбородку",               3, "12", 60),
            ("Гиперэкстензия",                  3, "15", 60),
        ],
    },
    {
        "label": "День B", "title": "Грудь + Трицепс", "subtitle": "Объём · Детали · Жим",
        "exercises": [
            ("Жим штанги на наклонной скамье",  4, "6–10", 90),
            ("Жим гантелей лёжа",              3, "10–12", 75),
            ("Кроссовер в кабельной раме",      3, "13–15", 60),
            ("Трицепсовый блок (верёвка)",      4, "12", 60),
            ("Французский жим лёжа",           3, "10–12", 60),
            ("Разведение гантелей лёжа",       3, "12–15", 60),
        ],
    },
    {
        "label": "День C", "title": "Ноги + Бицепс", "subtitle": "База · Руки · Пропорции",
        "exercises": [
            ("Приседания со штангой",           4, "6–10", 120),
            ("Румынская тяга",                  4, "10–12", 90),
            ("Жим ногами (платформа)",          3, "12–15", 75),
            ("Сгибание ног лёжа",              3, "12", 60),
            ("Сгибание рук со штангой",         4, "10–12", 60),
            ("Молотковые сгибания гантелями",   3, "12–14", 60),
        ],
    },
]


def run():
    db = SessionLocal()
    try:
        if db.query(Exercise).count() > 0:
            print("Already seeded, skipping.")
            return

        ex_map: dict[str, Exercise] = {}
        for data in EXERCISES:
            ex = Exercise(**data)
            db.add(ex)
            db.flush()
            ex_map[ex.name] = ex

        program = Program(
            name="V-Shape Plan",
            slug="v-shape",
            description="Программа на набор массы и формирование V-образного силуэта.",
            type="hypertrophy",
            days_per_week=3,
            difficulty="intermediate",
            goal="Набор массы",
        )
        db.add(program)
        db.flush()

        for day_num, day_data in enumerate(VSHAPE_DAYS, start=1):
            day = WorkoutDay(
                program_id=program.id,
                label=day_data["label"],
                title=day_data["title"],
                subtitle=day_data["subtitle"],
                day_number=day_num,
            )
            db.add(day)
            db.flush()

            for order, (ex_name, sets, reps, rest) in enumerate(day_data["exercises"]):
                ex = ex_map.get(ex_name)
                if not ex:
                    print(f"  WARNING: exercise not found: {ex_name}")
                    continue
                db.add(WorkoutExercise(
                    workout_day_id=day.id,
                    exercise_id=ex.id,
                    sets=sets,
                    reps=reps,
                    rest_seconds=rest,
                    order=order,
                ))

        db.commit()
        print("Seed complete.")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    run()
