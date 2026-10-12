from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.config import get_settings

settings = get_settings()

# The connection to the dabatase engine is established.
# The echo parameter tells the Engine program to log all the SQL it emits 
# to a Python logger that it will write to standard output.
engine = create_engine(settings.db_url.get_secret_value(), echo=settings.debug)

# A session factory is created
SessionLocal = sessionmaker(
    # Binds the Session to the engine, which manages database connections.
    bind=engine,
    
    # Prevents SQLAlchemy from automatically flushing pending changes
    # before executing queries.
    autoflush=False
)
    