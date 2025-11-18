from models import Base, engine, Session, Recipient

# Create all tables in the database (database.db will be created automatically if it doesn't exist)
Base.metadata.create_all(engine)

# Start a session to add recipients
session = Session()

# Add your real recipients
recipients = [
    Recipient(name="Narayana", email="lakshminarayanareddykota5@gmail.com"),
    Recipient(name="Mahesh", email="sejalamahesh@gmail.com")
]

for r in recipients:
    # Check if recipient already exists
    if not session.query(Recipient).filter_by(email=r.email).first():
        session.add(r)

session.commit()
print("Database initialized and recipients added successfully!")