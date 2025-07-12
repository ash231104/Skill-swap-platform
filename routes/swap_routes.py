from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.models import SwapRequest, User, db
from forms.forms import SwapRequestForm

bp = Blueprint('swap_routes', __name__)

@bp.route('/swaps', methods=['GET', 'POST'])
@login_required
def view_swaps():
    swaps = SwapRequest.query.filter((SwapRequest.sender_id == current_user.id) | (SwapRequest.receiver_id == current_user.id)).all()
    return render_template('swap_requests.html', swap_requests=swaps)

@bp.route('/swap/request/<int:user_id>', methods=['GET', 'POST'])
@login_required
def request_swap(user_id):
    form = SwapRequestForm()
    receiver = User.query.get_or_404(user_id)
    if form.validate_on_submit():
        new_request = SwapRequest(sender_id=current_user.id, receiver_id=receiver.id, skill=form.skill.data)
        db.session.add(new_request)
        db.session.commit()
        flash('Swap request sent!', 'success')
        return redirect(url_for('swap_routes.view_swaps'))
    return render_template('feedback.html', form=form)

@bp.route('/swap/delete/<int:swap_id>')
@login_required
def delete_swap(swap_id):
    swap = SwapRequest.query.get_or_404(swap_id)
    if swap.sender_id == current_user.id and swap.status == 'Pending':
        db.session.delete(swap)
        db.session.commit()
        flash('Swap request deleted.', 'info')
    return redirect(url_for('swap_routes.view_swaps'))