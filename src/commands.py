from datetime import datetime

from flask.cli import with_appcontext
import click
from src.ext import db
from src.models import User, Activity, Member, Slider

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")

    # User
    admin = User(username="admin", role="admin")
    admin.set_password("admin123")
    admin.create()

    activity = Activity(titile='',
                        description="საცხოვრებელი გარემო ისტორიული ცვლილებების აღქმის ერთგვარი პრიზმაა. მნიშვნელოვანი ისტორიული მოვლენების ტრადიციული ნარატივები,"
                                    " როგორც წესი, ფოკუსირებულია თარიღებზე, ძალაუფლების მქონე პირებსა და ისეთ მასშტაბურ კატეგორიებზე, როგორიცაა დემოკრატია, სოციალიზმი, "
                                    "ავტორიტარიზმი, მოდერნიზაცია და ა.შ. ამის საპირისპიროდ, მოცემული სემინარი ყურადღებას გაამახვილებს დიდ ისტორიულ ნაპრალზე"
                                    " — სსრკ-ის დაშლაზე — და ამ მოვლენას ურბანული ბინის „გამადიდებელი შუშის“ ქვეშ შეისწავლის, რათა გააანალიზოს რიგითი პოსტსაბჭოთა "
                                    "მოქალაქეების ყოველდღიური ცხოვრების ტრანსფორმაცია. კატერინა მალაია ისაუბრებს სახლში მიმდინარე ცვლილებების მიკვლევისა და დოკუმენტირების "
                                    "მეთოდოლოგიურ გამოწვევებზე და მათი გადაჭრის მისეულ გზებზე.",
                        datetime=datetime.now(),
                        timestamp=datetime.now().time(),
                        img="images/8f6887d9216742de9417acb708674035.png")
    activity.create()

    member = Member(name="ანა",
                    surname="ხიბია",
                    role="არქიტექტურის მკვლევარი",
                    academical_degree="არქიტექტურის მაგისტრანტი",
                    contribution="ანა ილიას სახელმწიფო უნივერსიტეტის არქიტექტურის ფაკულტეტის კურსდამთავრებულია და ამჟამად არქიტექტურის მაგისტრატურის საფეხურზე სწავლობს. მისი აკადემიური გამოცდილება ეფუძნება არქიტექტურულ დაპროექტებასა და "
                                 "სივრცით აზროვნებას, განსაკუთრებული ინტერესით კი შენობებს, საჯარო სივრცესა და ურბანულ გარემოს შორის "
                                 "არსებულ კავშირებს იკვლევს. სწავლის პროცესში მისი ინტერესის სფეროდ ჩამოყალიბდა"
                                 " იმის შესწავლა, თუ როგორ ვითარდება ქალაქები დროთა განმავლობაში"
                                 " და როგორ ახდენს გავლენას არქიტექტურული გადაწყვეტილებები ყოველდღიურ ცხოვრებაზე."
                                 " იგი განსაკუთრებით დაინტერესებულია ურბანული ფორმითა და არსებული საქალაქო სივრცეების ტრანსფორმაციით.",
                    image="images/5bef7002103c44a3b487bab638246e09.jpg")

    member.create()

    slider = Slider(img="images/c2f5bd220e874439b2a649e33c2902e7.jpg")
    slider.create()

    click.echo("Database populated!")

