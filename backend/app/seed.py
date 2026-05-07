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
    dict(name="Австралийские подтягивания", muscle_group="back",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         difficulty="beginner",
         technique="Низкая перекладина, тело горизонтально — тянешь грудь к перекладине. Хорошая прогрессия перед полными подтягиваниями."),
    dict(name="Тяга штанги в наклоне обратным хватом", muscle_group="back",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват снизу (супинация), наклон 45°, спина прямая. Тяни к поясу — акцент на нижние широчайшие и бицепс сильнее, чем при прямом хвате."),
    dict(name="Становая тяга", muscle_group="back",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         difficulty="advanced",
         technique="Штанга у голеней, стопы на ширине бёдер. Спина прямая, лопатки сведены. Тяни через пятки — бёдра и плечи поднимаются одновременно. Задействует всю заднюю цепь."),
    dict(name="Тяга гантелей лёжа лицом вниз", muscle_group="back",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Лёжа на наклонной скамье лицом вниз, тяни гантели вверх разводя локти. Акцент на ромбовидные и среднюю часть спины."),
    # ── CHEST ──
    dict(name="Жим штанги на наклонной скамье", muscle_group="chest",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Угол скамьи 30–45°. Хват чуть шире плеч, лопатки сведены и прижаты. Опускай медленно (2 сек). Жми взрывно вверх."),
    dict(name="Жим штанги лёжа", muscle_group="chest",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват чуть шире плеч. Лопатки сведены и прижаты к скамье. Опускай к нижней части груди. Жми взрывно."),
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
    # ── BACK (additional) ──
    dict(name="Тяга Т-грифа", muscle_group="back", types=["strength", "hypertrophy"], equipment=["barbell"], technique="Корпус наклонён ~45°, хват нейтральный. Тяните гриф к животу, сводя лопатки в конечной точке. Не округляйте поясницу."),
    dict(name="Тяга нижнего блока узким хватом", muscle_group="back", types=["hypertrophy"], equipment=["cable"], technique="Сидя, спина прямая, рукоять параллельным хватом. Тяните к пупку, локти вдоль корпуса. Полное растяжение в начале."),
    dict(name="Шраги со штангой", muscle_group="back", types=["hypertrophy"], equipment=["barbell"], technique="Штанга перед бёдрами, плечи поднимать строго вверх — без вращения. Фиксация 1 сек в верхней точке."),
    dict(name="Тяга гантели в наклоне двумя руками", muscle_group="back", types=["hypertrophy"], equipment=["dumbbells"], technique="Опора на скамью одной рукой и коленом. Тяга гантели вдоль корпуса, локоть выше спины в финале. Полная амплитуда."),
    dict(name="Подтягивания обратным хватом", muscle_group="back", types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"], technique="Ладони к себе, хват чуть уже плеч. Бицепс активно участвует. Подбородок выше перекладины, контролируемый спуск."),
    # ── CHEST (additional) ──
    dict(name="Жим гантелей на горизонтальной скамье", muscle_group="chest", types=["hypertrophy"], equipment=["dumbbells"], technique="Гантели над грудью, локти 45–75°. Полный диапазон: растяжение внизу, сведение вверху. Нейтральный поясничный прогиб."),
    dict(name="Жим в тренажёре (Хаммер)", muscle_group="chest", types=["hypertrophy"], equipment=["machine"], technique="Спина полностью прижата к спинке. Жмите ручки вперёд — не вверх. Медленный возврат 3–4 сек."),
    dict(name="Сведение в кроссовере снизу", muscle_group="chest", types=["hypertrophy"], equipment=["cable"], technique="Блок внизу, тяга вперёд-вверх по дуге. Акцент на верхнюю и среднюю часть груди. Руки слегка согнуты в локтях."),
    dict(name="Алмазные отжимания", muscle_group="chest", types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"], technique="Руки под грудью, большие и указательные пальцы образуют ромб. Локти двигаются назад, а не в стороны."),
    dict(name="Отжимания широким хватом", muscle_group="chest",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Руки шире плеч, локти уходят в стороны — акцент на грудь. Опускайся до касания грудью пола, жми взрывно вверх."),
    dict(name="Отжимания с ногами на возвышении", muscle_group="chest",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Ноги на скамье или ступеньке — угол смещает нагрузку на верхнюю часть груди. Локти уходят чуть в стороны."),
    dict(name="Жим штанги на наклонной вниз головой", muscle_group="chest",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Скамья под углом вниз, ноги зафиксированы. Хват чуть шире плеч. Акцент на нижнюю часть груди. Опускай к нижней части грудины."),
    dict(name="Сведение в тренажёре Pec Deck", muscle_group="chest",
         types=["hypertrophy"], equipment=["machine"],
         technique="Тренажёр «бабочка». Локти согнуты под 90°, прижаты к мягким упорам. Своди руки перед грудью — чистая изоляция без помощи трицепса."),
    # ── SHOULDERS (additional) ──
    dict(name="Тяга гантелей к подбородку", muscle_group="shoulders", types=["hypertrophy"], equipment=["dumbbells"], technique="Узкий хват, локти ведут движение выше плеч. Гантели держите близко к телу. Не запрокидывайте голову."),
    dict(name="Жим в тренажёре сидя (плечи)", muscle_group="shoulders", types=["hypertrophy"], equipment=["machine"], technique="Спина плотно к спинке. Жим строго вертикально, локти не уходят назад за линию корпуса."),
    dict(name="Разведение в стороны в кроссовере", muscle_group="shoulders", types=["hypertrophy"], equipment=["cable"], technique="Блоки на уровне бёдер, тяга в стороны до параллели с полом. Постоянное натяжение кабеля лучше гантелей."),
    dict(name="Обратные разведения в тренажёре (задняя дельта)", muscle_group="shoulders", types=["hypertrophy"], equipment=["machine"], technique="Тренажёр «бабочка» развёрнут лицом к подушке. Руки разводить горизонтально, акцент на заднюю дельту."),
    dict(name="Жим штанги сидя", muscle_group="shoulders",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Хват чуть шире плеч, штанга у верхней части груди. Жми строго вверх. Меньше нагрузки на поясницу чем стоя — удобнее контролировать технику."),
    dict(name="Тяга к подбородку в кроссовере", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["cable"],
         technique="Нижний блок, узкий хват. Тяни к подбородку — локти ведут движение выше кистей. Постоянное натяжение кабеля по всей амплитуде."),
    dict(name="Пайк-отжимания", muscle_group="shoulders",
         types=["strength", "calisthenics"], equipment=["bodyweight"],
         technique="Таз поднят вверх, тело в форме перевёрнутой V. Опускай голову к полу между руками — акцент на передние дельты и верх плеч."),
    dict(name="Стойка на руках у стены", muscle_group="shoulders",
         types=["strength", "calisthenics"], equipment=["bodyweight"],
         difficulty="advanced",
         technique="Упор руками в пол, ноги у стены. Удержание положения или полные отжимания в стойке. Максимальная нагрузка на плечи с собственным весом."),
    dict(name="Разведение в стороны в тренажёре (сидя)", muscle_group="shoulders",
         types=["hypertrophy"], equipment=["machine"],
         technique="Тренажёр для средней дельты. Сидя, руки на упорах. Фиксированная траектория обеспечивает чистую изоляцию без читинга."),
    # ── BICEPS (additional) ──
    dict(name="Сгибание на блоке стоя", muscle_group="biceps", types=["hypertrophy"], equipment=["cable"], technique="Нижний блок, прямая рукоять. Постоянное натяжение по всей амплитуде. Локти прижаты к корпусу."),
    dict(name="Попеременные сгибания гантелей с супинацией", muscle_group="biceps", types=["hypertrophy"], equipment=["dumbbells"], technique="В нижней точке ладонь смотрит внутрь, в верхней — разворачивается к потолку. Максимальное сокращение бицепса."),
    dict(name="Сгибание со штангой обратным хватом", muscle_group="biceps", types=["hypertrophy"], equipment=["barbell"], technique="Хват сверху (пронация). Акцент на брахиалис и брахиорадиалис. Локти неподвижны, поясница не включается."),
    dict(name="Сгибания с EZ-грифом", muscle_group="biceps",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="EZ-гриф снижает нагрузку на запястья и локтевые суставы. Хват под углом — естественное положение рук. Локти прижаты к телу, подъём до полного сокращения."),
    dict(name="Сгибания на блоке одной рукой", muscle_group="biceps",
         types=["hypertrophy"], equipment=["cable"],
         technique="Нижний блок, одна рука. Постоянное натяжение по всей амплитуде — хорошо для пика бицепса. В верхней точке — пауза и максимальное сокращение."),
    dict(name="Подтягивания обратным хватом (акцент бицепс)", muscle_group="biceps",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Ладони к себе, хват уже плеч. Тяни грудь к перекладине — бицепс работает как основная тянущая сила. Контролируемый спуск до полного выпрямления рук."),
    dict(name="Сгибания гантелями на наклонной скамье", muscle_group="biceps",
         types=["hypertrophy"], equipment=["dumbbells"],
         technique="Лёжа спиной на наклонной скамье, руки свисают вниз. Увеличенный диапазон растяжки бицепса в нижней точке. Медленное опускание — не теряй напряжение."),
    # ── TRICEPS (additional) ──
    dict(name="Разгибание на блоке прямой рукоятью", muscle_group="triceps", types=["hypertrophy"], equipment=["cable"], technique="Верхний блок, локти прижаты к бокам. Полное разгибание до «щелчка» трицепса. Не раскачивайте корпус."),
    dict(name="Отжимания на трицепс (обратные)", muscle_group="triceps", types=["hypertrophy", "calisthenics"], equipment=["bodyweight"], technique="Руки на скамье позади, ноги вытянуты. Опускайтесь до 90° в локтях, выжимайте за счёт трицепса."),
    dict(name="Разгибание гантели двумя руками из-за головы", muscle_group="triceps", types=["hypertrophy"], equipment=["dumbbells"], technique="Сидя, одна гантель двумя руками за головой. Локти смотрят в потолок, движение только в локтевом суставе."),
    dict(name="Отжимания на брусьях узким хватом", muscle_group="triceps",
         types=["strength", "hypertrophy", "calisthenics"], equipment=["bodyweight"],
         technique="Руки ближе к корпусу, корпус вертикально без наклона вперёд — акцент уходит с груди на трицепс. Локти двигаются назад, полное разгибание вверху."),
    dict(name="Французский жим стоя с EZ-грифом", muscle_group="triceps",
         types=["hypertrophy"], equipment=["barbell"],
         technique="Стоя, EZ-гриф за головой. Локти фиксированы у головы, двигаются только в локтевом суставе. Разгибай вверх — акцент на длинную головку трицепса."),
    dict(name="Разгибание на блоке одной рукой", muscle_group="triceps",
         types=["hypertrophy"], equipment=["cable"],
         technique="Верхний блок, одна рука, нейтральный хват. Локоть зафиксирован у головы. Полное разгибание вниз — максимальное растяжение длинной головки."),
    # ── QUADRICEPS (additional) ──
    dict(name="Гакк-приседания", muscle_group="quadriceps", types=["hypertrophy"], equipment=["machine"], technique="Ноги на платформе, стопы на ширине плеч. Колени над носками, спина прижата. Акцент на квадрицепс."),
    dict(name="Выпады вперёд", muscle_group="quadriceps", types=["hypertrophy", "strength"], equipment=["bodyweight", "dumbbells"], technique="Шаг вперёд, заднее колено почти касается пола. Переднее колено не выходит за носок. Корпус вертикально."),
    dict(name="Жим одной ногой (платформа)", muscle_group="quadriceps", types=["hypertrophy"], equipment=["machine"], technique="Одна нога по центру платформы. Позволяет исправить дисбаланс между ногами. Контролируемый спуск."),
    dict(name="Приседания в Смите", muscle_group="quadriceps", types=["hypertrophy", "strength"], equipment=["machine"], technique="Штанга в тренажёре Смита, ноги чуть впереди. Безопаснее для поясницы, позволяет работать с большим весом."),
    dict(name="Приседания с собственным весом", muscle_group="quadriceps",
         types=["hypertrophy", "calisthenics"], equipment=["bodyweight"],
         difficulty="beginner",
         technique="Стопы чуть шире плеч, носки развёрнуты наружу, спина прямая. Приседай до параллели с полом. Хорошо для новичков и разминки."),
    dict(name="Приседания сумо", muscle_group="quadriceps",
         types=["strength", "hypertrophy"], equipment=["barbell", "dumbbells"],
         technique="Широкая постановка ног, носки сильно развёрнуты наружу. Акцент на внутреннюю поверхность бедра и ягодицы. Спина прямая, колени над носками."),
    dict(name="Выпады в сторону", muscle_group="quadriceps",
         types=["hypertrophy", "calisthenics"], equipment=["bodyweight", "dumbbells"],
         technique="Широкий шаг в сторону, приседаешь на эту ногу — другая прямая. Акцент на внутреннюю поверхность бедра и приводящие. Корпус вертикально."),
    dict(name="Зашагивания на платформу", muscle_group="quadriceps",
         types=["strength", "hypertrophy"], equipment=["bodyweight", "dumbbells"],
         technique="Шагаешь на скамью или степ-платформу, полностью выпрямляя ногу вверху. Акцент на квадрицепс и ягодицы. Не отталкивайся задней ногой."),
    dict(name="Приседания в прыжке", muscle_group="quadriceps",
         types=["calisthenics", "cardio"], equipment=["bodyweight"],
         technique="Обычное приседание с взрывным выпрыгиванием вверх. Приземляйся мягко, перекатом с носка на пятку. Развивает взрывную силу."),
    # ── HAMSTRINGS (additional) ──
    dict(name="Сгибание ног стоя в тренажёре", muscle_group="hamstrings", types=["hypertrophy"], equipment=["machine"], technique="Одна нога, таз прижат к тренажёру. Полное сгибание, медленный контролируемый возврат 3 сек."),
    dict(name="Становая тяга на прямых ногах", muscle_group="hamstrings", types=["strength", "hypertrophy"], equipment=["barbell", "dumbbells"], technique="Ноги почти прямые, штанга вдоль голеней. Наклон до горизонтали, спина нейтральная. Чувствуйте растяжение бицепса бедра."),
    dict(name="Ягодичный мостик", muscle_group="hamstrings", types=["hypertrophy", "strength"], equipment=["barbell", "bodyweight"], technique="Лёжа, ноги согнуты, штанга на бёдрах. Подъём таза до прямой линии, сжатие ягодиц в верхней точке."),
    dict(name="Становая тяга (акцент бицепс бедра)", muscle_group="hamstrings",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         difficulty="advanced",
         technique="Штанга у голеней, стопы на ширине бёдер. Спина прямая, лопатки сведены. Тяни через пятки — бицепс бедра, ягодицы и поясница работают как основные движители."),
    dict(name="Гудмонинг со штангой", muscle_group="hamstrings",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Штанга на трапециях, ноги чуть согнуты. Наклон вперёд с прямой спиной до параллели с полом — растяжка бицепса бедра под нагрузкой. Медленно и контролируемо."),
    dict(name="Сгибание ног сидя в тренажёре", muscle_group="hamstrings",
         types=["hypertrophy"], equipment=["machine"],
         technique="Сидя, бицепс бедра в растянутом положении в начале движения. Сгибай до полного сокращения, медленный контролируемый возврат."),
    dict(name="Мёртвая тяга с гантелями", muscle_group="hamstrings",
         types=["strength", "hypertrophy"], equipment=["dumbbells"],
         technique="Гантели у бёдер, лёгкий сгиб в коленях. Наклоняйся вперёд отводя таз назад — до растяжки бицепса бедра. Проще контролировать технику чем со штангой."),
    dict(name="Nordic curl (скандинавские сгибания)", muscle_group="hamstrings",
         types=["strength", "calisthenics"], equipment=["bodyweight"],
         difficulty="advanced",
         technique="Колени на полу, ноги зафиксированы партнёром или упором. Медленно опускайся вперёд удерживая тело прямым — максимальная нагрузка на бицепс бедра в эксцентрике."),
    # ── CALVES (additional) ──
    dict(name="Подъём на носки сидя в тренажёре", muscle_group="calves", types=["hypertrophy"], equipment=["machine"], technique="Акцент на камбаловидную мышцу (нога согнута). Полная амплитуда: растяжение внизу, полное сокращение вверху."),
    dict(name="Подъём на носки с гантелями", muscle_group="calves", types=["hypertrophy"], equipment=["dumbbells"], technique="Стоя, гантели в руках. Подниматься высоко на носках, задержка 1–2 сек. Можно выполнять на возвышении."),
    dict(name="Подъём на носки на одной ноге", muscle_group="calves", types=["strength", "calisthenics"], equipment=["bodyweight"], technique="Одна нога, опора рукой. Медленный темп 2-2-2. Отлично устраняет асимметрию икр."),
    # ── CORE (additional) ──
    dict(name="Велосипед лёжа", muscle_group="core", types=["hypertrophy", "cardio"], equipment=["bodyweight"], technique="Лёжа, ноги в воздухе. Попеременно подтягиваете колено к противоположному локтю. Поясница прижата к полу."),
    dict(name="Русские скручивания", muscle_group="core", types=["hypertrophy"], equipment=["bodyweight", "dumbbells"], technique="Сидя, корпус 45°, ноги приподняты. Поворот корпуса вправо-влево. Можно держать гантель или блин."),
    dict(name="Складка на пресс", muscle_group="core", types=["hypertrophy", "calisthenics"], equipment=["bodyweight"], technique="Лёжа, одновременно поднимаете ноги и корпус навстречу друг другу. Пика — руки тянутся к носкам."),
    # ── LOWER BACK (additional) ──
    dict(name="Становая тяга сумо", muscle_group="lower_back", types=["strength", "hypertrophy"], equipment=["barbell"], technique="Широкая стойка, носки развёрнуты 45°. Меньше нагрузки на поясницу чем классика. Бёдра и ягодицы активно включаются."),
    dict(name="Обратные гиперэкстензии", muscle_group="lower_back", types=["hypertrophy"], equipment=["machine", "bodyweight"], technique="Лицом вниз на тренажёре, ноги свисают. Подъём ног до горизонтали. Акцент на ягодицы и низ спины."),
    dict(name="Доброе утро (Good Morning)", muscle_group="lower_back", types=["strength", "hypertrophy"], equipment=["barbell"], technique="Штанга на трапециях. Наклон вперёд с прямой спиной до ~45°. Движение в тазобедренном суставе, не в пояснице."),
    # ── TRAPS ──
    dict(name="Шраги с гантелями", muscle_group="traps", types=["hypertrophy"], equipment=["dumbbells"], technique="Гантели вдоль тела, плечи поднимать строго вверх. Без вращения. Задержка 1–2 сек в пиковом сокращении."),
    dict(name="Шраги в тренажёре Смита", muscle_group="traps", types=["hypertrophy"], equipment=["machine"], technique="Фиксированная траектория позволяет работать с большим весом и сосредоточиться на сокращении трапеций."),
    dict(name="Фермерская ходьба", muscle_group="traps", types=["strength", "hypertrophy"], equipment=["dumbbells", "barbell"], technique="Тяжёлые гантели/гири в руках, ходьба на дистанцию. Трапеции статически нагружены всё время. Плечи не опускать."),
    # ── FOREARMS ──
    dict(name="Сгибание запястий со штангой", muscle_group="forearms", types=["hypertrophy"], equipment=["barbell"], technique="Предплечья на скамье, ладони вверх. Сгибание кисти с полной амплитудой. Медленное движение, лёгкий вес."),
    dict(name="Разгибание запястий со штангой", muscle_group="forearms", types=["hypertrophy"], equipment=["barbell"], technique="Предплечья на скамье, ладони вниз. Разгибание кисти. Акцент на тыльную сторону предплечья."),
    dict(name="Удержание блина", muscle_group="forearms", types=["strength"], equipment=["barbell"], technique="Зажать блин (10–25 кг) кончиками пальцев и удерживать до отказа. Лучшее упражнение на силу хвата."),
    # ── GLUTES ──
    dict(name="Ягодичный мостик в тренажёре", muscle_group="glutes", types=["hypertrophy"], equipment=["machine"], technique="Специальный тренажёр для мостика. Позволяет работать с большим весом безопасно. Фокус на сжатии ягодиц."),
    dict(name="Отведение ноги в кроссовере", muscle_group="glutes", types=["hypertrophy"], equipment=["cable", "bodyweight"], technique="Манжета на щиколотке у нижнего блока или стоя у опоры. Отводить ногу назад-вверх. Корпус слегка наклонён вперёд, не раскачивайтесь."),
    dict(name="Сумо-приседания с гантелью", muscle_group="glutes", types=["hypertrophy"], equipment=["dumbbells"], technique="Широкая стойка, носки 45°, гантель между ног. Акцент на ягодицы и приводящие мышцы. Колени над носками."),
    dict(name="Гипертрастер (Kickback) в тренажёре", muscle_group="glutes", types=["hypertrophy"], equipment=["machine"], technique="Стоя лицом к тренажёру, толкать платформу назад-вверх ягодичным усилием. Нога почти прямая в пике."),
    dict(name="Ягодичный мостик с собственным весом", muscle_group="glutes",
         types=["hypertrophy", "calisthenics"], equipment=["bodyweight"],
         difficulty="beginner",
         technique="Лёжа на спине, колени согнуты, стопы на полу. Поднимай таз вверх сжимая ягодицы — пауза 2 сек вверху. Базовое упражнение для новичков и разминки."),
    dict(name="Становая тяга (акцент ягодицы)", muscle_group="glutes",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         difficulty="advanced",
         technique="Штанга у голеней, стопы на ширине бёдер. Спина прямая. В верхней точке — полное разгибание с акцентом на сжатие ягодиц. Тяни через пятки."),
    dict(name="Выпады назад", muscle_group="glutes",
         types=["hypertrophy", "calisthenics"], equipment=["bodyweight", "dumbbells"],
         technique="Шаг назад вместо вперёд — меньше нагрузки на колено, больше акцент на ягодицы. Опускай заднее колено к полу, корпус вертикально."),
    dict(name="Приседания сумо со штангой", muscle_group="glutes",
         types=["strength", "hypertrophy"], equipment=["barbell"],
         technique="Широкая постановка ног, носки сильно развёрнуты наружу. По сравнению с обычными приседаниями сильнее включает ягодицы и внутреннюю поверхность бедра."),
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
