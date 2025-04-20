from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash("Please log in to access this page.", "warning")
                return redirect(url_for('login'))
            if roles:
                user_role = session.get('role', '').lower()
                allowed_roles = [r.lower() for r in roles]
                if user_role not in allowed_roles:
                    flash("You don't have permission to access this page.", "danger")
                    return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
