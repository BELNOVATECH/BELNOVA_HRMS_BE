from typing import Optional
import datetime
import decimal

from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Date, DateTime, ForeignKeyConstraint, Index, Integer, Numeric, PrimaryKeyConstraint, String, Table, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class HolidayCalendar(Base):
    __tablename__ = 'holiday_calendar'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_holiday_calendar_id'),
        UniqueConstraint('holiday_name', 'holiday_date', name='uq_holiday_name_date')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    holiday_name: Mapped[str] = mapped_column(String(255), nullable=False)
    holiday_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))


class MasterBank(Base):
    __tablename__ = 'master_bank'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_bank_id'),
        UniqueConstraint('bank_name', name='uk_master_bank_bank_name')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    bank_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='bank')


class MasterBloodGroup(Base):
    __tablename__ = 'master_blood_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_blood_group_id'),
        UniqueConstraint('blood_group', name='uk_master_blood_group_blood_group')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    blood_group: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='blood_group')


class MasterDepartment(Base):
    __tablename__ = 'master_department'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_department_id'),
        UniqueConstraint('department', name='uk_master_department_department')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    department: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    master_designation: Mapped[list['MasterDesignation']] = relationship('MasterDesignation', back_populates='dept')
    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='department')
    job_openings: Mapped[list['JobOpenings']] = relationship('JobOpenings', back_populates='department')


class MasterEmpStatus(Base):
    __tablename__ = 'master_emp_status'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_emp_status_id'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='status')


class MasterEmployeeType(Base):
    __tablename__ = 'master_employee_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_employee_type_id'),
        UniqueConstraint('employee_type', name='uk_master_employee_type_employee_type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_type: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='employee_type')


class MasterGender(Base):
    __tablename__ = 'master_gender'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_gender_id'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gender: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='gender')


class MasterLeavetype(Base):
    __tablename__ = 'master_leavetype'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_leavetype_id'),
        UniqueConstraint('leave_type', name='uk_master_leavetype_leave_type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    leave_type: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    granted: Mapped[Optional[int]] = mapped_column(Integer)

    leave_request: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', back_populates='leavetype')


class MasterMaritalStatus(Base):
    __tablename__ = 'master_marital_status'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_marital_status_id'),
        UniqueConstraint('name', name='uk_master_marital_status_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='marital_status')


class MasterModule(Base):
    __tablename__ = 'master_module'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_module_id'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_name: Mapped[str] = mapped_column(String(255), nullable=False)
    order_by: Mapped[Optional[int]] = mapped_column(Integer)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    master_screen: Mapped[list['MasterScreen']] = relationship('MasterScreen', back_populates='module')
    master_sub_module: Mapped[list['MasterSubModule']] = relationship('MasterSubModule', back_populates='module')
    master_screen_permission: Mapped[list['MasterScreenPermission']] = relationship('MasterScreenPermission', back_populates='module')
    employee_activity: Mapped[list['EmployeeActivity']] = relationship('EmployeeActivity', back_populates='module')


class MasterMonth(Base):
    __tablename__ = 'master_month'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_month_id'),
        UniqueConstraint('month_name', name='uk_master_month_month_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    month_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    payslips: Mapped[list['Payslips']] = relationship('Payslips', back_populates='month')


class MasterOccupation(Base):
    __tablename__ = 'master_occupation'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_occupation_id'),
        UniqueConstraint('occupation_name', name='uk_master_occupation_occupation_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    occupation_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_family_member: Mapped[list['EmployeeFamilyMember']] = relationship('EmployeeFamilyMember', back_populates='occupation')


class MasterPaymethod(Base):
    __tablename__ = 'master_paymethod'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_paymethod_id'),
        UniqueConstraint('paymethod', name='uk_master_paymethod_paymethod')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    paymethod: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))


class MasterPercCalId(Base):
    __tablename__ = 'master_perc_cal_id'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_perc_calc_id'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    basic_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    conveyance_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    medical_allowance_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    special_allowance_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    arrears_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total_earnings_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    pf_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    esic_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    pt_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    tds_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    other_deductions_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total_deductions_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    gross_earning_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    deduction_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    net_pay_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    net_pay_in_words_perc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    hra_perc: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    payslips: Mapped[list['Payslips']] = relationship('Payslips', back_populates='perc_cal')


class MasterProject(Base):
    __tablename__ = 'master_project'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_project_id'),
        UniqueConstraint('project_name', name='uk_master_project')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    master_project_module: Mapped[list['MasterProjectModule']] = relationship('MasterProjectModule', back_populates='project')
    tasks: Mapped[list['Tasks']] = relationship('Tasks', back_populates='project')
    task_history: Mapped[list['TaskHistory']] = relationship('TaskHistory', back_populates='project')


class MasterRelation(Base):
    __tablename__ = 'master_relation'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_relation_id'),
        UniqueConstraint('relation_type', name='uk_master_relation_relation_type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    relation_type: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    employee_family_member: Mapped[list['EmployeeFamilyMember']] = relationship('EmployeeFamilyMember', back_populates='relation')


class MasterRole(Base):
    __tablename__ = 'master_role'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_role_id'),
        UniqueConstraint('role_name', name='uk_master_shift_role_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    users: Mapped[list['Users']] = relationship('Users', back_populates='role')
    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='role')
    master_screen_permission: Mapped[list['MasterScreenPermission']] = relationship('MasterScreenPermission', back_populates='role')


class MasterSession(Base):
    __tablename__ = 'master_session'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_session_id'),
        UniqueConstraint('session_name', name='uk_master_session_session_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    leave_request_from_date_session: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.from_date_session_id]', back_populates='from_date_session')
    leave_request_to_date_session: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.to_date_session_id]', back_populates='to_date_session')


class MasterShift(Base):
    __tablename__ = 'master_shift'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_shift_id'),
        UniqueConstraint('shift_type', name='uk_master_shift_shift_type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    shift_type: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))


class MasterStage(Base):
    __tablename__ = 'master_stage'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_stage_id'),
        UniqueConstraint('stage_name', name='uk_master_stage_stage_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    stage_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    interview_scheduled: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', back_populates='stage')
    interview_scheduled_history: Mapped[list['InterviewScheduledHistory']] = relationship('InterviewScheduledHistory', back_populates='stage')


class MasterStatus(Base):
    __tablename__ = 'master_status'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_status_id'),
        UniqueConstraint('name', name='uk_master_status_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    job_openings: Mapped[list['JobOpenings']] = relationship('JobOpenings', back_populates='status')
    candidate_applied: Mapped[list['CandidateApplied']] = relationship('CandidateApplied', back_populates='application_status')
    leave_request: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', back_populates='status')
    tasks: Mapped[list['Tasks']] = relationship('Tasks', back_populates='status')
    interview_scheduled: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', back_populates='status')
    interview_scheduled_history: Mapped[list['InterviewScheduledHistory']] = relationship('InterviewScheduledHistory', back_populates='status')


class MasterTaskType(Base):
    __tablename__ = 'master_task_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_task_type_id'),
        UniqueConstraint('task_type', name='uk_master_task_type_task_type')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_type: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    tasks: Mapped[list['Tasks']] = relationship('Tasks', back_populates='task_type')


class MasterWorkLocation(Base):
    __tablename__ = 'master_work_location'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_work_location_id'),
        UniqueConstraint('work_location', name='uk_master_work_location_work_location')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    work_location: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))


class MasterWorkingStatus(Base):
    __tablename__ = 'master_working_status'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_working_status_id'),
        UniqueConstraint('name', name='uk_master_working_status_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    attendance_tracker: Mapped[list['AttendanceTracker']] = relationship('AttendanceTracker', back_populates='working_status')


class MasterYear(Base):
    __tablename__ = 'master_year'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_master_year_id'),
        UniqueConstraint('year_name', name='uk_master_year_year_name')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    year_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    payslips: Mapped[list['Payslips']] = relationship('Payslips', back_populates='year')



t_vw_performance_rating = Table(
    'vw_performance_rating', Base.metadata,
    Column('id', BigInteger),
    Column('emp_id', Integer),
    Column('employee_name', String),
    Column('designation_id', Integer),
    Column('designation_name', String(255)),
    Column('rating', Numeric(2, 1)),
    Column('reviewer_id', Integer),
    Column('reviewer_name', String),
    Column('created_date', DateTime)
)


t_vw_recent_activity = Table(
    'vw_recent_activity', Base.metadata,
    Column('emp_id', Integer),
    Column('employee_name', String),
    Column('module_id', Integer),
    Column('module_name', String(255)),
    Column('sub_module_id', Integer),
    Column('sub_module_name', String(255)),
    Column('created_date', String),
    Column('activity_description', String(255))
)


t_vw_screen_permission_list = Table(
    'vw_screen_permission_list', Base.metadata,
    Column('module_id', Integer),
    Column('module_name', String(255)),
    Column('sub_module_id', Integer),
    Column('sub_module_name', String(255)),
    Column('role_id', Integer),
    Column('fa_fa_icon', String(500)),
    Column('routes', String(255)),
    Column('can_view', Boolean),
    Column('can_edit', Boolean),
    Column('can_delete', Boolean),
    Column('can_access', Boolean),
    Column('can_update', Boolean)
)


t_vw_task_history_details = Table(
    'vw_task_history_details', Base.metadata,
    Column('task_id', BigInteger),
    Column('title', String(255)),
    Column('emp_id', BigInteger),
    Column('employee_name', String),
    Column('project_id', Integer),
    Column('project_name', String(255)),
    Column('reporting_manager_id', BigInteger),
    Column('reporting_manager_name', String),
    Column('comments', String),
    Column('rating', Integer),
    Column('efforts_in_days', Integer),
    Column('description', Text),
    Column('from_assignee_id', BigInteger),
    Column('to_assignee_id', BigInteger),
    Column('project_module_id', Integer),
    Column('project_module', String(255))
)


class MasterDesignation(Base):
    __tablename__ = 'master_designation'
    __table_args__ = (
        ForeignKeyConstraint(['dept_id'], ['master_department.id'], name='fk_master_designation_dept_id'),
        PrimaryKeyConstraint('id', name='pk_master_designation_id'),
        UniqueConstraint('designation_name', 'dept_id', name='uk_master_designation_designation_name_dept_id'),
        Index('idx_master_designation_dept_id', 'dept_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    designation_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    dept_id: Mapped[Optional[int]] = mapped_column(Integer)

    dept: Mapped[Optional['MasterDepartment']] = relationship('MasterDepartment', back_populates='master_designation')
    employee_registration: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', back_populates='designation')
    job_openings: Mapped[list['JobOpenings']] = relationship('JobOpenings', back_populates='designation')
    candidate_applied: Mapped[list['CandidateApplied']] = relationship('CandidateApplied', back_populates='designation')
    employee_rating: Mapped[list['EmployeeRating']] = relationship('EmployeeRating', back_populates='designation')
    interview_scheduled: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', back_populates='designation')


class MasterProjectModule(Base):
    __tablename__ = 'master_project_module'
    __table_args__ = (
        ForeignKeyConstraint(['project_id'], ['master_project.id'], name='fk_master_project_module_project_id'),
        PrimaryKeyConstraint('id', name='pk_master_project_module_id'),
        Index('idx_master_project_module_project_id', 'project_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_module: Mapped[str] = mapped_column(String(255), nullable=False)
    project_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    project: Mapped['MasterProject'] = relationship('MasterProject', back_populates='master_project_module')
    tasks: Mapped[list['Tasks']] = relationship('Tasks', back_populates='project_module')
    task_history: Mapped[list['TaskHistory']] = relationship('TaskHistory', back_populates='project_module')


class MasterScreen(Base):
    __tablename__ = 'master_screen'
    __table_args__ = (
        ForeignKeyConstraint(['module_id'], ['master_module.id'], name='master_screen_module_id_fkey'),
        PrimaryKeyConstraint('id', name='master_screen_pkey'),
        Index('idx_master_screen_module_id', 'module_id'),
        Index('ix_master_screen_id', 'id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    screen_name: Mapped[str] = mapped_column(String, nullable=False)
    screen_label: Mapped[Optional[str]] = mapped_column(String)
    fa_fa_icon: Mapped[Optional[str]] = mapped_column(String)
    routes: Mapped[Optional[str]] = mapped_column(String)
    module_id: Mapped[Optional[int]] = mapped_column(Integer)
    order_by: Mapped[Optional[int]] = mapped_column(Integer)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)

    module: Mapped[Optional['MasterModule']] = relationship('MasterModule', back_populates='master_screen')


class MasterSubModule(Base):
    __tablename__ = 'master_sub_module'
    __table_args__ = (
        ForeignKeyConstraint(['module_id'], ['master_module.id'], name='fk_master_sub_module_module_id'),
        PrimaryKeyConstraint('id', name='pk_master_sub_module_id'),
        Index('idx_master_sub_module_module_id', 'module_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sub_module_name: Mapped[str] = mapped_column(String(255), nullable=False)
    module_id: Mapped[Optional[int]] = mapped_column(Integer)
    screen_label: Mapped[Optional[str]] = mapped_column(String(255))
    fa_fa_icon: Mapped[Optional[str]] = mapped_column(String(500))
    routes: Mapped[Optional[str]] = mapped_column(String(255))
    order_by: Mapped[Optional[int]] = mapped_column(Integer)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    module: Mapped[Optional['MasterModule']] = relationship('MasterModule', back_populates='master_sub_module')
    master_screen_permission: Mapped[list['MasterScreenPermission']] = relationship('MasterScreenPermission', back_populates='sub_module')
    employee_activity: Mapped[list['EmployeeActivity']] = relationship('EmployeeActivity', back_populates='sub_module')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['role_id'], ['master_role.id'], name='users_role_id_fkey'),
        PrimaryKeyConstraint('id', name='users_pkey'),
        Index('idx_users_role_id', 'role_id'),
        Index('ix_users_email', 'email', unique=True),
        Index('ix_users_id', 'id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, nullable=False)
    mobile: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    gender_id: Mapped[Optional[int]] = mapped_column(Integer)
    dob: Mapped[Optional[datetime.date]] = mapped_column(Date)
    address: Mapped[Optional[str]] = mapped_column(String)
    created_by: Mapped[Optional[int]] = mapped_column(Integer)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    modified_by: Mapped[Optional[int]] = mapped_column(Integer)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)

    role: Mapped['MasterRole'] = relationship('MasterRole', back_populates='users')


class EmployeeRegistration(Base):
    __tablename__ = 'employee_registration'
    __table_args__ = (
        ForeignKeyConstraint(['bank_id'], ['master_bank.id'], name='fk_employee_registration_bank_id'),
        ForeignKeyConstraint(['blood_group_id'], ['master_blood_group.id'], name='fk_employee_registration_blood_group_id'),
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_employee_registration_created_by'),
        ForeignKeyConstraint(['department_id'], ['master_department.id'], name='fk_employee_registration_department_id'),
        ForeignKeyConstraint(['designation_id'], ['master_designation.id'], name='fk_employee_registration_designation_id'),
        ForeignKeyConstraint(['employee_type_id'], ['master_employee_type.id'], name='fk_employee_registration_work_status_id'),
        ForeignKeyConstraint(['gender_id'], ['master_gender.id'], name='fk_employee_registration_gender_id'),
        ForeignKeyConstraint(['manager_id'], ['employee_registration.id'], name='fk_employee_registration_manager_id'),
        ForeignKeyConstraint(['marital_status_id'], ['master_marital_status.id'], name='fk_employee_registration_civil_status_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_employee_registration_modified_by'),
        ForeignKeyConstraint(['role_id'], ['master_role.id'], name='fk_employee_registration_role_id'),
        ForeignKeyConstraint(['status_id'], ['master_emp_status.id'], name='fk_employee_registration_status_id'),
        PrimaryKeyConstraint('id', name='pk_employee_registration_id'),
        UniqueConstraint('aadhaar', name='uk_employee_aadhaar'),
        UniqueConstraint('bank_ac_no', name='uk_employee_bank'),
        UniqueConstraint('email', name='uk_employee_email'),
        UniqueConstraint('mobile', name='uk_employee_mobile'),
        UniqueConstraint('pan', name='uk_employee_pan'),
        UniqueConstraint('uan', name='uk_employee_uan'),
        Index('idx_employee_registration_bank_id', 'bank_id'),
        Index('idx_employee_registration_blood_group_id', 'blood_group_id'),
        Index('idx_employee_registration_created_by', 'created_by'),
        Index('idx_employee_registration_department_id', 'department_id'),
        Index('idx_employee_registration_designation_id', 'designation_id'),
        Index('idx_employee_registration_employee_type_id', 'employee_type_id'),
        Index('idx_employee_registration_gender_id', 'gender_id'),
        Index('idx_employee_registration_manager_id', 'manager_id'),
        Index('idx_employee_registration_marital_status_id', 'marital_status_id'),
        Index('idx_employee_registration_modified_by', 'modified_by'),
        Index('idx_employee_registration_role_id', 'role_id'),
        Index('idx_employee_registration_status_id', 'status_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    marital_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    gender_id: Mapped[int] = mapped_column(Integer, nullable=False)
    mobile: Mapped[str] = mapped_column(String(20), nullable=False)
    designation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, nullable=False)
    employee_type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    salary: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    join_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    ctc: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    password: Mapped[str] = mapped_column(String(500), nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    present_address: Mapped[Optional[str]] = mapped_column(Text)
    date_of_birth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    emergency_mobile: Mapped[Optional[str]] = mapped_column(String(20))
    hired_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    manager_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    upload_doc: Mapped[Optional[str]] = mapped_column(String(500))
    bank_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    bank_ac_no: Mapped[Optional[str]] = mapped_column(String(50))
    ifsc_code: Mapped[Optional[str]] = mapped_column(String)
    esic: Mapped[Optional[str]] = mapped_column(String(50))
    pan: Mapped[Optional[str]] = mapped_column(String(50))
    emp_code: Mapped[Optional[str]] = mapped_column(String(100))
    uan: Mapped[Optional[str]] = mapped_column(String(20))
    father_name: Mapped[Optional[str]] = mapped_column(String(255))
    blood_group_id: Mapped[Optional[int]] = mapped_column(Integer)
    permanent_address: Mapped[Optional[str]] = mapped_column(String(255))
    role_id: Mapped[Optional[int]] = mapped_column(Integer)
    work_location_id: Mapped[Optional[int]] = mapped_column(Integer)
    shift_id: Mapped[Optional[int]] = mapped_column(Integer)
    probation_end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    aadhaar: Mapped[Optional[str]] = mapped_column(String(15))
    reference_mobile: Mapped[Optional[str]] = mapped_column(String(15))
    pf_ac_no: Mapped[Optional[str]] = mapped_column(String(50))

    bank: Mapped[Optional['MasterBank']] = relationship('MasterBank', back_populates='employee_registration')
    blood_group: Mapped[Optional['MasterBloodGroup']] = relationship('MasterBloodGroup', back_populates='employee_registration')
    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[id], foreign_keys=[created_by], back_populates='employee_registration_reverse')
    employee_registration_reverse: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[created_by], foreign_keys=[created_by], back_populates='employee_registration')
    department: Mapped['MasterDepartment'] = relationship('MasterDepartment', back_populates='employee_registration')
    designation: Mapped['MasterDesignation'] = relationship('MasterDesignation', back_populates='employee_registration')
    employee_type: Mapped['MasterEmployeeType'] = relationship('MasterEmployeeType', back_populates='employee_registration')
    gender: Mapped['MasterGender'] = relationship('MasterGender', back_populates='employee_registration')
    manager: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[id], foreign_keys=[manager_id], back_populates='manager_reverse')
    manager_reverse: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[manager_id], foreign_keys=[manager_id], back_populates='manager')
    marital_status: Mapped['MasterMaritalStatus'] = relationship('MasterMaritalStatus', back_populates='employee_registration')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[id], foreign_keys=[modified_by], back_populates='employee_registration__reverse')
    employee_registration__reverse: Mapped[list['EmployeeRegistration']] = relationship('EmployeeRegistration', remote_side=[modified_by], foreign_keys=[modified_by], back_populates='employee_registration_')
    role: Mapped[Optional['MasterRole']] = relationship('MasterRole', back_populates='employee_registration')
    status: Mapped['MasterEmpStatus'] = relationship('MasterEmpStatus', back_populates='employee_registration')
    attendance_tracker_created_by: Mapped[list['AttendanceTracker']] = relationship('AttendanceTracker', foreign_keys='[AttendanceTracker.created_by]', back_populates='employee_registration')
    attendance_tracker_emp: Mapped[list['AttendanceTracker']] = relationship('AttendanceTracker', foreign_keys='[AttendanceTracker.emp_id]', back_populates='emp')
    attendance_tracker_modified_by: Mapped[list['AttendanceTracker']] = relationship('AttendanceTracker', foreign_keys='[AttendanceTracker.modified_by]', back_populates='employee_registration_')
    candidate_applied_created_by: Mapped[list['CandidateApplied']] = relationship('CandidateApplied', foreign_keys='[CandidateApplied.created_by]', back_populates='employee_registration')
    candidate_applied_modified_by: Mapped[list['CandidateApplied']] = relationship('CandidateApplied', foreign_keys='[CandidateApplied.modified_by]', back_populates='employee_registration_')
    employee_activity: Mapped[list['EmployeeActivity']] = relationship('EmployeeActivity', back_populates='emp')
    employee_family_member: Mapped[list['EmployeeFamilyMember']] = relationship('EmployeeFamilyMember', back_populates='emp')
    employee_rating_emp: Mapped[list['EmployeeRating']] = relationship('EmployeeRating', foreign_keys='[EmployeeRating.emp_id]', back_populates='emp')
    employee_rating_reviewer: Mapped[list['EmployeeRating']] = relationship('EmployeeRating', foreign_keys='[EmployeeRating.reviewer_id]', back_populates='reviewer')
    leave_request_approver: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.approver_id]', back_populates='approver')
    leave_request_created_by: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.created_by]', back_populates='employee_registration')
    leave_request_emp: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.emp_id]', back_populates='emp')
    leave_request_modified_by: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.modified_by]', back_populates='employee_registration_')
    leave_request_reporting_manager: Mapped[list['LeaveRequest']] = relationship('LeaveRequest', foreign_keys='[LeaveRequest.reporting_manager_id]', back_populates='reporting_manager')
    payslips_created_by: Mapped[list['Payslips']] = relationship('Payslips', foreign_keys='[Payslips.created_by]', back_populates='employee_registration')
    payslips_emp: Mapped[list['Payslips']] = relationship('Payslips', foreign_keys='[Payslips.emp_id]', back_populates='emp')
    payslips_modified_by: Mapped[list['Payslips']] = relationship('Payslips', foreign_keys='[Payslips.modified_by]', back_populates='employee_registration_')
    tasks: Mapped[list['Tasks']] = relationship('Tasks', back_populates='emp')
    interview_scheduled_created_by: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', foreign_keys='[InterviewScheduled.created_by]', back_populates='employee_registration')
    interview_scheduled_modified_by: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', foreign_keys='[InterviewScheduled.modified_by]', back_populates='employee_registration_')
    leave_request_cc_cc_to: Mapped[list['LeaveRequestCc']] = relationship('LeaveRequestCc', foreign_keys='[LeaveRequestCc.cc_to_id]', back_populates='cc_to')
    leave_request_cc_created_by: Mapped[list['LeaveRequestCc']] = relationship('LeaveRequestCc', foreign_keys='[LeaveRequestCc.created_by]', back_populates='employee_registration')
    leave_request_cc_modified_by: Mapped[list['LeaveRequestCc']] = relationship('LeaveRequestCc', foreign_keys='[LeaveRequestCc.modified_by]', back_populates='employee_registration_')
    task_history_emp: Mapped[list['TaskHistory']] = relationship('TaskHistory', foreign_keys='[TaskHistory.emp_id]', back_populates='emp')
    task_history_from_assignee: Mapped[list['TaskHistory']] = relationship('TaskHistory', foreign_keys='[TaskHistory.from_assignee_id]', back_populates='from_assignee')
    task_history_reporting_manager: Mapped[list['TaskHistory']] = relationship('TaskHistory', foreign_keys='[TaskHistory.reporting_manager_id]', back_populates='reporting_manager')
    task_history_to_assignee: Mapped[list['TaskHistory']] = relationship('TaskHistory', foreign_keys='[TaskHistory.to_assignee_id]', back_populates='to_assignee')


class JobOpenings(Base):
    __tablename__ = 'job_openings'
    __table_args__ = (
        ForeignKeyConstraint(['department_id'], ['master_department.id'], name='fk_job_openings_department_id'),
        ForeignKeyConstraint(['designation_id'], ['master_designation.id'], name='fk_job_openings_designation_id'),
        ForeignKeyConstraint(['status_id'], ['master_status.id'], name='fk_job_openings_status_id'),
        PrimaryKeyConstraint('id', name='pk_job_openings_id'),
        UniqueConstraint('department_id', 'designation_id', name='uk_job_openings_designation_id_department_id'),
        Index('idx_job_openings_department_id', 'department_id'),
        Index('idx_job_openings_designation_id', 'designation_id'),
        Index('idx_job_openings_status_id', 'status_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    designation_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    department_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    department: Mapped['MasterDepartment'] = relationship('MasterDepartment', back_populates='job_openings')
    designation: Mapped['MasterDesignation'] = relationship('MasterDesignation', back_populates='job_openings')
    status: Mapped['MasterStatus'] = relationship('MasterStatus', back_populates='job_openings')


class MasterScreenPermission(Base):
    __tablename__ = 'master_screen_permission'
    __table_args__ = (
        ForeignKeyConstraint(['module_id'], ['master_module.id'], name='fk_master_screen_permission_module_id'),
        ForeignKeyConstraint(['role_id'], ['master_role.id'], name='fk_master_screen_permission_role_id'),
        ForeignKeyConstraint(['sub_module_id'], ['master_sub_module.id'], name='fk_master_screen_permission_sub_module_id'),
        PrimaryKeyConstraint('id', name='pk_master_screen_permission_id'),
        UniqueConstraint('module_id', 'sub_module_id', 'role_id', name='uk_master_screen_permission_module_screen_role_id'),
        Index('idx_master_screen_permission_module_id', 'module_id'),
        Index('idx_master_screen_permission_role_id', 'role_id'),
        Index('idx_master_screen_permission_sub_module_id', 'sub_module_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    module_id: Mapped[Optional[int]] = mapped_column(Integer)
    sub_module_id: Mapped[Optional[int]] = mapped_column(Integer)
    role_id: Mapped[Optional[int]] = mapped_column(Integer)
    can_view: Mapped[Optional[bool]] = mapped_column(Boolean)
    can_edit: Mapped[Optional[bool]] = mapped_column(Boolean)
    can_delete: Mapped[Optional[bool]] = mapped_column(Boolean)
    can_access: Mapped[Optional[bool]] = mapped_column(Boolean)
    can_update: Mapped[Optional[bool]] = mapped_column(Boolean)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    module: Mapped[Optional['MasterModule']] = relationship('MasterModule', back_populates='master_screen_permission')
    role: Mapped[Optional['MasterRole']] = relationship('MasterRole', back_populates='master_screen_permission')
    sub_module: Mapped[Optional['MasterSubModule']] = relationship('MasterSubModule', back_populates='master_screen_permission')


class AttendanceTracker(Base):
    __tablename__ = 'attendance_tracker'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_attendance_tracker_created_by'),
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_attendance_tracker_emp_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_attendance_tracker_modified_by'),
        ForeignKeyConstraint(['working_status_id'], ['master_working_status.id'], name='fk_attendance_tracker_working_status_id'),
        PrimaryKeyConstraint('id', name='pk_attendance_tracker_id'),
        Index('idx_attendance_tracker_created_by', 'created_by'),
        Index('idx_attendance_tracker_emp_id', 'emp_id'),
        Index('idx_attendance_tracker_modified_by', 'modified_by'),
        Index('idx_attendance_tracker_working_status_id', 'working_status_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    attendance_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    working_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    check_in_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    check_out_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    working_hours: Mapped[Optional[datetime.timedelta]] = mapped_column(INTERVAL)
    remarks: Mapped[Optional[str]] = mapped_column(String(100))
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    check_in_latitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 6))
    check_in_longitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 6))
    check_out_latitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 6))
    check_out_longitude: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 6))

    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='attendance_tracker_created_by')
    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[emp_id], back_populates='attendance_tracker_emp')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='attendance_tracker_modified_by')
    working_status: Mapped['MasterWorkingStatus'] = relationship('MasterWorkingStatus', back_populates='attendance_tracker')


class CandidateApplied(Base):
    __tablename__ = 'candidate_applied'
    __table_args__ = (
        ForeignKeyConstraint(['application_status_id'], ['master_status.id'], name='fk_candidate_applied_application_status_id'),
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_candidate_applied_created_by'),
        ForeignKeyConstraint(['designation_id'], ['master_designation.id'], name='fk_candidate_applied_designation_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_candidate_applied_modified_by'),
        PrimaryKeyConstraint('id', name='pk_candidate_applied_id'),
        Index('idx_candidate_applied_application_status_id', 'application_status_id'),
        Index('idx_candidate_applied_created_by', 'created_by'),
        Index('idx_candidate_applied_designation_id', 'designation_id'),
        Index('idx_candidate_applied_modified_by', 'modified_by')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    candidate_name: Mapped[str] = mapped_column(String(255), nullable=False)
    designation_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    application_status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    mobile: Mapped[str] = mapped_column(String(15), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    dob: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    upload_resume: Mapped[Optional[str]] = mapped_column(String(500))
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    application_status: Mapped['MasterStatus'] = relationship('MasterStatus', back_populates='candidate_applied')
    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='candidate_applied_created_by')
    designation: Mapped['MasterDesignation'] = relationship('MasterDesignation', back_populates='candidate_applied')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='candidate_applied_modified_by')
    interview_scheduled: Mapped[list['InterviewScheduled']] = relationship('InterviewScheduled', back_populates='candidate')


class EmployeeActivity(Base):
    __tablename__ = 'employee_activity'
    __table_args__ = (
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_employee_activity_emp_id'),
        ForeignKeyConstraint(['module_id'], ['master_module.id'], name='fk_employee_activity_module_id'),
        ForeignKeyConstraint(['sub_module_id'], ['master_sub_module.id'], name='fk_employee_activity_sub_module_id'),
        PrimaryKeyConstraint('id', name='pk_employee_activity_id'),
        Index('idx_employee_activity_emp_id', 'emp_id'),
        Index('idx_employee_activity_module_id', 'module_id'),
        Index('idx_employee_activity_sub_module_id', 'sub_module_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(Integer, nullable=False)
    module_id: Mapped[int] = mapped_column(Integer, nullable=False)
    sub_module_id: Mapped[int] = mapped_column(Integer, nullable=False)
    activity_description: Mapped[str] = mapped_column(String(255), nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', back_populates='employee_activity')
    module: Mapped['MasterModule'] = relationship('MasterModule', back_populates='employee_activity')
    sub_module: Mapped['MasterSubModule'] = relationship('MasterSubModule', back_populates='employee_activity')


class EmployeeFamilyMember(Base):
    __tablename__ = 'employee_family_member'
    __table_args__ = (
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_employee_family_member_emp_id'),
        ForeignKeyConstraint(['occupation_id'], ['master_occupation.id'], name='fk_employee_family_member_occupation_id'),
        ForeignKeyConstraint(['relation_id'], ['master_relation.id'], name='fk_employee_family_member_relation_id'),
        PrimaryKeyConstraint('id', name='pk_employee_family_member_id'),
        Index('idx_employee_family_member_emp_id', 'emp_id'),
        Index('idx_employee_family_member_occupation_id', 'occupation_id'),
        Index('idx_employee_family_member_relation_id', 'relation_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(Integer, nullable=False)
    relation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    date_of_birth: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    occupation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    present_address: Mapped[str] = mapped_column(String(255), nullable=False)
    permanent_address: Mapped[str] = mapped_column(String(255), nullable=False)
    aadhaar: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    bank_account: Mapped[Optional[str]] = mapped_column(String(255))
    ifsc_code: Mapped[Optional[str]] = mapped_column(String(255))
    pan: Mapped[Optional[str]] = mapped_column(String(255))
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', back_populates='employee_family_member')
    occupation: Mapped['MasterOccupation'] = relationship('MasterOccupation', back_populates='employee_family_member')
    relation: Mapped['MasterRelation'] = relationship('MasterRelation', back_populates='employee_family_member')


class EmployeeRating(Base):
    __tablename__ = 'employee_rating'
    __table_args__ = (
        ForeignKeyConstraint(['designation_id'], ['master_designation.id'], name='fk_employee_rating_designation_id'),
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_employee_rating_emp_id'),
        ForeignKeyConstraint(['reviewer_id'], ['employee_registration.id'], name='fk_employee_rating_reviewer_id'),
        PrimaryKeyConstraint('id', name='pk_employee_rating_id'),
        Index('idx_employee_rating_designation_id', 'designation_id'),
        Index('idx_employee_rating_emp_id', 'emp_id'),
        Index('idx_employee_rating_reviewer_id', 'reviewer_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(Integer, nullable=False)
    designation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[decimal.Decimal] = mapped_column(Numeric(2, 1), nullable=False)
    reviewer_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    designation: Mapped['MasterDesignation'] = relationship('MasterDesignation', back_populates='employee_rating')
    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[emp_id], back_populates='employee_rating_emp')
    reviewer: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[reviewer_id], back_populates='employee_rating_reviewer')


class LeaveRequest(Base):
    __tablename__ = 'leave_request'
    __table_args__ = (
        ForeignKeyConstraint(['approver_id'], ['employee_registration.id'], name='fk_leave_request_approver_id'),
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_leave_request_created_by'),
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_leave_request_emp_id'),
        ForeignKeyConstraint(['from_date_session_id'], ['master_session.id'], name='fk_leave_request_from_date_session_id'),
        ForeignKeyConstraint(['leavetype_id'], ['master_leavetype.id'], name='fk_leave_request_leavetype_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_leave_request_modified_by'),
        ForeignKeyConstraint(['reporting_manager_id'], ['employee_registration.id'], name='fk_leave_request_reporting_manager_id'),
        ForeignKeyConstraint(['status_id'], ['master_status.id'], name='fk_leave_request_status_id'),
        ForeignKeyConstraint(['to_date_session_id'], ['master_session.id'], name='fk_leave_request_to_date_session_id'),
        PrimaryKeyConstraint('id', name='pk_leave_request_id'),
        Index('idx_leave_request_approver_id', 'approver_id'),
        Index('idx_leave_request_created_by', 'created_by'),
        Index('idx_leave_request_emp_id', 'emp_id'),
        Index('idx_leave_request_from_date_session_id', 'from_date_session_id'),
        Index('idx_leave_request_leavetype_id', 'leavetype_id'),
        Index('idx_leave_request_modified_by', 'modified_by'),
        Index('idx_leave_request_reporting_manager_id', 'reporting_manager_id'),
        Index('idx_leave_request_status_id', 'status_id'),
        Index('idx_leave_request_to_date_session_id', 'to_date_session_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    leavetype_id: Mapped[int] = mapped_column(Integer, nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    reporting_manager_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    mobile: Mapped[str] = mapped_column(String(15), nullable=False)
    total_days: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(5, 1))
    reason: Mapped[Optional[str]] = mapped_column(String(255))
    status_id: Mapped[Optional[int]] = mapped_column(Integer)
    approver_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    remarks: Mapped[Optional[str]] = mapped_column(String(255))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    from_date_session_id: Mapped[Optional[int]] = mapped_column(Integer)
    to_date_session_id: Mapped[Optional[int]] = mapped_column(Integer)
    upload_file: Mapped[Optional[str]] = mapped_column(String(500))
    approved_on: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    approver: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[approver_id], back_populates='leave_request_approver')
    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='leave_request_created_by')
    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[emp_id], back_populates='leave_request_emp')
    from_date_session: Mapped[Optional['MasterSession']] = relationship('MasterSession', foreign_keys=[from_date_session_id], back_populates='leave_request_from_date_session')
    leavetype: Mapped['MasterLeavetype'] = relationship('MasterLeavetype', back_populates='leave_request')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='leave_request_modified_by')
    reporting_manager: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[reporting_manager_id], back_populates='leave_request_reporting_manager')
    status: Mapped[Optional['MasterStatus']] = relationship('MasterStatus', back_populates='leave_request')
    to_date_session: Mapped[Optional['MasterSession']] = relationship('MasterSession', foreign_keys=[to_date_session_id], back_populates='leave_request_to_date_session')
    leave_request_cc: Mapped[list['LeaveRequestCc']] = relationship('LeaveRequestCc', back_populates='leave_request')


class Payslips(Base):
    __tablename__ = 'payslips'
    __table_args__ = (
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_payslips_created_by'),
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_payslips_emp_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_payslips_modified_by'),
        ForeignKeyConstraint(['month_id'], ['master_month.id'], name='fk_payslips_month_id'),
        ForeignKeyConstraint(['perc_cal_id'], ['master_perc_cal_id.id'], name='fk_payslips_perc_cal_id'),
        ForeignKeyConstraint(['year_id'], ['master_year.id'], name='fk_payslips_year_id'),
        PrimaryKeyConstraint('id', name='pk_payslips_id'),
        UniqueConstraint('emp_id', 'month_id', 'year_id', name='uk_payslips_emp_id_month_id_year_id'),
        Index('idx_payslips_created_by', 'created_by'),
        Index('idx_payslips_emp_id', 'emp_id'),
        Index('idx_payslips_modified_by', 'modified_by'),
        Index('idx_payslips_month_id', 'month_id'),
        Index('idx_payslips_perc_cal_id', 'perc_cal_id'),
        Index('idx_payslips_year_id', 'year_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    emp_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    month_id: Mapped[int] = mapped_column(Integer, nullable=False)
    year_id: Mapped[int] = mapped_column(Integer, nullable=False)
    basic: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    conveyance: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    hra: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    medical_allowance: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    special_allowance: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total_days: Mapped[Optional[int]] = mapped_column(Integer)
    paid_days: Mapped[Optional[int]] = mapped_column(Integer)
    lop_days: Mapped[Optional[int]] = mapped_column(Integer)
    arrears: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    total_earnings: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    pf: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    esic: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    pt: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    tds: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    other_deductions: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    total_deductions: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    gross_earning: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    deduction: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    net_pay: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 2))
    net_pay_in_words: Mapped[Optional[str]] = mapped_column(String(500))
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    perc_cal_id: Mapped[Optional[int]] = mapped_column(Integer)

    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='payslips_created_by')
    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[emp_id], back_populates='payslips_emp')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='payslips_modified_by')
    month: Mapped['MasterMonth'] = relationship('MasterMonth', back_populates='payslips')
    perc_cal: Mapped[Optional['MasterPercCalId']] = relationship('MasterPercCalId', back_populates='payslips')
    year: Mapped['MasterYear'] = relationship('MasterYear', back_populates='payslips')


class Tasks(Base):
    __tablename__ = 'tasks'
    __table_args__ = (
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_tasks_emp_id'),
        ForeignKeyConstraint(['project_id'], ['master_project.id'], name='fk_tasks_project_id'),
        ForeignKeyConstraint(['project_module_id'], ['master_project_module.id'], name='fk_tasks_project_module_id'),
        ForeignKeyConstraint(['status_id'], ['master_status.id'], name='fk_tasks_status_id'),
        ForeignKeyConstraint(['task_type_id'], ['master_task_type.id'], name='fk_tasks_task_type_id'),
        PrimaryKeyConstraint('id', name='pk_tasks_id'),
        UniqueConstraint('title', 'task_type_id', 'project_id', 'emp_id', 'status_id', name='uk_tasks_title_task_type_id_project_id_emp_id_status_id'),
        Index('idx_tasks_emp_id', 'emp_id'),
        Index('idx_tasks_project_id', 'project_id'),
        Index('idx_tasks_project_module_id', 'project_module_id'),
        Index('idx_tasks_status_id', 'status_id'),
        Index('idx_tasks_task_type_id', 'task_type_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    task_type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    project_id: Mapped[int] = mapped_column(Integer, nullable=False)
    emp_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    due_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    reporting_manager_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    task_manager_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    efforts_in_days: Mapped[Optional[int]] = mapped_column(Integer)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    project_module_id: Mapped[Optional[int]] = mapped_column(BigInteger)

    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', back_populates='tasks')
    project: Mapped['MasterProject'] = relationship('MasterProject', back_populates='tasks')
    project_module: Mapped[Optional['MasterProjectModule']] = relationship('MasterProjectModule', back_populates='tasks')
    status: Mapped['MasterStatus'] = relationship('MasterStatus', back_populates='tasks')
    task_type: Mapped['MasterTaskType'] = relationship('MasterTaskType', back_populates='tasks')
    task_history: Mapped[list['TaskHistory']] = relationship('TaskHistory', back_populates='task')


class InterviewScheduled(Base):
    __tablename__ = 'interview_scheduled'
    __table_args__ = (
        ForeignKeyConstraint(['candidate_id'], ['candidate_applied.id'], name='fk_interview_scheduled_candidate_id'),
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_interview_scheduled_created_by'),
        ForeignKeyConstraint(['designation_id'], ['master_designation.id'], name='fk_interview_scheduled_designation_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_interview_scheduled_modified_by'),
        ForeignKeyConstraint(['stage_id'], ['master_stage.id'], name='fk_interview_scheduled_stage_id'),
        ForeignKeyConstraint(['status_id'], ['master_status.id'], name='fk_interview_scheduled_status_id'),
        PrimaryKeyConstraint('id', name='pk_interview_scheduled_id'),
        Index('idx_interview_scheduled_candidate_id', 'candidate_id'),
        Index('idx_interview_scheduled_created_by', 'created_by'),
        Index('idx_interview_scheduled_designation_id', 'designation_id'),
        Index('idx_interview_scheduled_modified_by', 'modified_by'),
        Index('idx_interview_scheduled_stage_id', 'stage_id'),
        Index('idx_interview_scheduled_status_id', 'status_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    candidate_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    interview_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    stage_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    designation_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    feedback: Mapped[Optional[str]] = mapped_column(String(255))
    rating: Mapped[Optional[str]] = mapped_column(String(20))
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    candidate: Mapped['CandidateApplied'] = relationship('CandidateApplied', back_populates='interview_scheduled')
    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='interview_scheduled_created_by')
    designation: Mapped['MasterDesignation'] = relationship('MasterDesignation', back_populates='interview_scheduled')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='interview_scheduled_modified_by')
    stage: Mapped['MasterStage'] = relationship('MasterStage', back_populates='interview_scheduled')
    status: Mapped['MasterStatus'] = relationship('MasterStatus', back_populates='interview_scheduled')
    interview_scheduled_history: Mapped[list['InterviewScheduledHistory']] = relationship('InterviewScheduledHistory', back_populates='interview_scheduled')


class LeaveRequestCc(Base):
    __tablename__ = 'leave_request_cc'
    __table_args__ = (
        ForeignKeyConstraint(['cc_to_id'], ['employee_registration.id'], name='fk_leave_request_cc_cc_to_id'),
        ForeignKeyConstraint(['created_by'], ['employee_registration.id'], name='fk_leave_request_cc_created_by'),
        ForeignKeyConstraint(['leave_request_id'], ['leave_request.id'], name='fk_leave_request_cc_leave_request_id'),
        ForeignKeyConstraint(['modified_by'], ['employee_registration.id'], name='fk_leave_request_cc_modified_by'),
        PrimaryKeyConstraint('id', name='pk_leave_request_cc_id'),
        Index('idx_leave_request_cc_cc_to_id', 'cc_to_id'),
        Index('idx_leave_request_cc_created_by', 'created_by'),
        Index('idx_leave_request_cc_leave_request_id', 'leave_request_id'),
        Index('idx_leave_request_cc_modified_by', 'modified_by')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    leave_request_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    cc_to_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    cc_to: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[cc_to_id], back_populates='leave_request_cc_cc_to')
    employee_registration: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[created_by], back_populates='leave_request_cc_created_by')
    leave_request: Mapped['LeaveRequest'] = relationship('LeaveRequest', back_populates='leave_request_cc')
    employee_registration_: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[modified_by], back_populates='leave_request_cc_modified_by')


class TaskHistory(Base):
    __tablename__ = 'task_history'
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='ck_task_history_rating'),
        ForeignKeyConstraint(['emp_id'], ['employee_registration.id'], name='fk_task_history_emp_id'),
        ForeignKeyConstraint(['from_assignee_id'], ['employee_registration.id'], name='fk_task_history_from_assignee_id'),
        ForeignKeyConstraint(['project_id'], ['master_project.id'], name='fk_task_history_project_id'),
        ForeignKeyConstraint(['project_module_id'], ['master_project_module.id'], name='fk_task_history_project_module_id'),
        ForeignKeyConstraint(['reporting_manager_id'], ['employee_registration.id'], name='fk_task_history_reporting_manager_id'),
        ForeignKeyConstraint(['task_id'], ['tasks.id'], name='fk_task_history_task_id'),
        ForeignKeyConstraint(['to_assignee_id'], ['employee_registration.id'], name='fk_task_history_to_assignee_id'),
        PrimaryKeyConstraint('id', name='pk_task_history_id'),
        Index('idx_task_history_emp_id', 'emp_id'),
        Index('idx_task_history_from_assignee_id', 'from_assignee_id'),
        Index('idx_task_history_project_id', 'project_id'),
        Index('idx_task_history_project_module_id', 'project_module_id'),
        Index('idx_task_history_reporting_manager_id', 'reporting_manager_id'),
        Index('idx_task_history_task_id', 'task_id'),
        Index('idx_task_history_to_assignee_id', 'to_assignee_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    task_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    emp_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    project_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    from_assignee_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    to_assignee_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    reporting_manager_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    comments: Mapped[Optional[str]] = mapped_column(String)
    rating: Mapped[Optional[int]] = mapped_column(Integer)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    project_module_id: Mapped[Optional[int]] = mapped_column(BigInteger)

    emp: Mapped['EmployeeRegistration'] = relationship('EmployeeRegistration', foreign_keys=[emp_id], back_populates='task_history_emp')
    from_assignee: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[from_assignee_id], back_populates='task_history_from_assignee')
    project: Mapped['MasterProject'] = relationship('MasterProject', back_populates='task_history')
    project_module: Mapped[Optional['MasterProjectModule']] = relationship('MasterProjectModule', back_populates='task_history')
    reporting_manager: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[reporting_manager_id], back_populates='task_history_reporting_manager')
    task: Mapped['Tasks'] = relationship('Tasks', back_populates='task_history')
    to_assignee: Mapped[Optional['EmployeeRegistration']] = relationship('EmployeeRegistration', foreign_keys=[to_assignee_id], back_populates='task_history_to_assignee')


class InterviewScheduledHistory(Base):
    __tablename__ = 'interview_scheduled_history'
    __table_args__ = (
        ForeignKeyConstraint(['interview_scheduled_id'], ['interview_scheduled.id'], name='fk_interview_scheduled_history_interview_scheduled_id'),
        ForeignKeyConstraint(['stage_id'], ['master_stage.id'], name='fk_interview_scheduled_history_stage_id'),
        ForeignKeyConstraint(['status_id'], ['master_status.id'], name='fk_interview_scheduled_history_status_id'),
        PrimaryKeyConstraint('id', name='pk_interview_scheduled_history_id'),
        Index('idx_interview_scheduled_history_interview_scheduled_id', 'interview_scheduled_id'),
        Index('idx_interview_scheduled_history_stage_id', 'stage_id'),
        Index('idx_interview_scheduled_history_status_id', 'status_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    interview_scheduled_id: Mapped[int] = mapped_column(Integer, nullable=False)
    stage_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('now()'))
    modified_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    interview_scheduled: Mapped['InterviewScheduled'] = relationship('InterviewScheduled', back_populates='interview_scheduled_history')
    stage: Mapped['MasterStage'] = relationship('MasterStage', back_populates='interview_scheduled_history')
    status: Mapped['MasterStatus'] = relationship('MasterStatus', back_populates='interview_scheduled_history')
