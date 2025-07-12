from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models.models import User, SwapRequest, AdminLog, db

bp = Blueprint('admin_routes', __name__)

@bp.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Unauthorized", 'danger')
        return redirect(url_for('user_routes.dashboard'))
    return render_template('admin.html')

@bp.route('/admin/users')
@login_required
def view_users():
    if not current_user.is_admin:
        return redirect(url_for('user_routes.dashboard'))
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@bp.route('/admin/swaps')
@login_required
def view_swaps():
    if not current_user.is_admin:
        return redirect(url_for('user_routes.dashboard'))
    swaps = SwapRequest.query.all()
    return render_template('admin_swaps.html', swaps=swaps)

@bp.route('/admin/ban/<int:user_id>')
@login_required
def ban_user(user_id):
    if not current_user.is_admin:
        return redirect(url_for('user_routes.dashboard'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User banned and deleted.', 'warning')
    return redirect(url_for('admin_routes.view_users'))